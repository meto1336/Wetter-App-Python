from importlib.resources import path
from deep_translator import GoogleTranslator
import requests
import urllib
import urllib.request
from io import BytesIO
from PIL import Image, ImageTk
import time
import customtkinter
import tkinter as tk
import tkinter.messagebox
from urllib.request import urlopen

customtkinter.set_appearance_mode("system") 
customtkinter.set_default_color_theme("blue")  


def get_weather_information(city):
    api_key = 'c026d4d627f8ce702228f47f3d2de872'
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + api_key
    result = requests.get(url)
    data = result.json()
    print(data)
    try:
        temp = data['main']['temp']
        icon = data['weather'][0]['icon']
        description = data['weather'][0]['description']
        country = data['sys']['country']
        image_link = "https://openweathermap.org/img/wn/" + icon + ".png"
        weather_values = [temp, description, country, image_link]
        return weather_values
    except:
        tk.messagebox.showerror(title="Fehler", message="Die Stadt existiert nicht")
    
def display_weather_information():
    city_name = city_entry.get()
    if city_name == "":
         tk.messagebox.showerror(title="Fehler", message="Das Feld darf nicht leer")
    else:
        weather = get_weather_information(city_name)
        rounded_temp = round(weather[0])
        capitalize_description = str(weather[1])
        translated_descripton = GoogleTranslator(source='en', target='de').translate(capitalize_description)
        temp_label.configure(text=str(rounded_temp) + ' ° C')
        city_label.configure(text= city_name.capitalize() + ', ' + weather[2])
        description_label.configure(text=translated_descripton.title())
        URL = weather[3]
        u = urlopen(URL)
        raw_data = u.read()
        u.close()
        path = ImageTk.PhotoImage(data=raw_data)
        weather_image.configure(image=path)
        weather_image.photo = path # anchor the image to the object.

    
app = customtkinter.CTk()

app.title('Wetter App')
app.geometry('600x400')
app.resizable(False, False)

city_entry = customtkinter.CTkEntry(app, width=150, height=30, placeholder_text="Stadt eingeben...")
city_entry.pack(pady=20)

city_search = customtkinter.CTkButton(app, text='Suche Wetter', text_font=('Roboto', 12), command=display_weather_information)
city_search.pack(pady=10)

city_label = customtkinter.CTkLabel(app, text='', text_font=('Roboto', 17))
city_label.pack(pady=20)

weather_image = customtkinter.CTkLabel(app, image="", text='')
weather_image.pack(pady=40)

temp_label = customtkinter.CTkLabel(app, text='', text_font=('Roboto', 17))
temp_label.pack(pady=10)

description_label = customtkinter.CTkLabel(app, text='', text_font=('Roboto', 17))
description_label.pack(pady=10)


app.mainloop()

