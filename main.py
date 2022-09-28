from email.mime import image
from itertools import count
from deep_translator import GoogleTranslator
import tkinter as ttk
from tkinter import *
import requests
import urllib
import io
from PIL import Image, ImageDraw, ImageTk




def get_weather_information(city):
    api_key = 'c026d4d627f8ce702228f47f3d2de872'
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + api_key
    r = requests.get(url)
    data = r.json()
    temp = data['main']['temp']
    icon = data['weather'][0]['icon']
    description = data['weather'][0]['description']
    country = data['sys']['country']
    weather_values = [icon, temp, description, country]
    
    return weather_values
    
def display_weather_information():
    city_name = city_entry.get()
    weather = get_weather_information(city_name)
    rounded_temp = round(weather[1])
    capitalize_description = str(weather[2])
    translated_descripton = GoogleTranslator(source='en', target='de').translate(capitalize_description)
    image_link = "https://openweathermap.org/img/wn/" + weather[0] + ".png"
    #print(io.BytesIO(urllib.request.urlopen(image_link).read()))
    picture = Image.open(io.BytesIO(urllib.request.urlopen(image_link).read()))
    weather_image['image'] = ImageTk.PhotoImage(str(picture))
    temp_label['text'] = str(rounded_temp) + ' ° C'
    city_label['text'] = city_name.capitalize() + ', ' + weather[3]
    description_label['text'] = translated_descripton.title()
    
    
app = ttk.Tk()

app.title('Wetter App')
app.geometry('600x500')

city_entry = ttk.Entry(app)
city_entry.pack(pady=20)

city_search = ttk.Button(app, text='Suche Wetter', command=display_weather_information)
city_search.pack(pady=10)

city_label = ttk.Label(app, text='', font=('bold', 17))
city_label.pack(pady=20)

weather_image = ttk.Label(app, image="")
weather_image.pack(pady=40)

temp_label = ttk.Label(app, text='', font=('bold', 17))
temp_label.pack(pady=10)

description_label = ttk.Label(app, text='', font=('bold', 17))
description_label.pack(pady=10)


app.mainloop()

