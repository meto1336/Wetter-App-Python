from email.mime import image
from importlib.resources import path
from itertools import count
import tkinter
from turtle import back
from deep_translator import GoogleTranslator
import tkinter as ttk
from tkinter import *
import requests
import urllib
import urllib.request
import io
from PIL import Image, ImageTk
import time


def get_weather_information(city):
    api_key = 'c026d4d627f8ce702228f47f3d2de872'
    url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=' + api_key
    r = requests.get(url)
    data = r.json()
    temp = data['main']['temp']
    icon = data['weather'][0]['icon']
    description = data['weather'][0]['description']
    country = data['sys']['country']
    #image_link = "https://openweathermap.org/img/wn/" + icon + ".png"
    #image_link = "https://upload.wikimedia.org/wikipedia/de/thumb/b/bb/Png-logo.png/800px-Png-logo.png"
    picture_path = "test.png"
    try:
        urllib.request.urlretrieve('https://upload.wikimedia.org/wikipedia/de/thumb/b/bb/Png-logo.png/800px-Png-logo.png', picture_path)
    except:
        print('Network Issue')
    weather_values = [temp, description, country]
    
    return weather_values
    
def display_weather_information():
    city_name = city_entry.get()
    if city_name == "":
        print("Das Feld darf nicht leer sein")
    else:
        weather = get_weather_information(city_name)
        rounded_temp = round(weather[0])
        capitalize_description = str(weather[1])
        translated_descripton = GoogleTranslator(source='en', target='de').translate(capitalize_description)
        #picture = urllib.request.urlretriever(image_link, savein)
        #picture = Image.open(urllib.request.urlopen(image_link).read())
        temp_label['text'] = str(rounded_temp) + ' ° C'
        city_label['text'] = city_name.capitalize() + ', ' + weather[2]
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
weather_image['image'] = ImageTk.PhotoImage(Image.open('test.png'))
weather_image.pack(pady=40)

temp_label = ttk.Label(app, text='', font=('bold', 17))
temp_label.pack(pady=10)

description_label = ttk.Label(app, text='', font=('bold', 17))
description_label.pack(pady=10)


app.mainloop()

