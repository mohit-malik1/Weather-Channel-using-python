from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import json
import requests
import io
import base64
from urllib.request import urlopen

#2

def readweather(city):
    readweather=requests.get('https://api.worldweatheronline.com/premium/v1/weather.ashx?key=a325e17cbfa2437a886191115192205&q='+city+'&format=json') #we have to generate API after 60 days (starting 23 may)
    data=json.loads(readweather.text)

    #Determining Current Temperature
    date=data['data']['weather'][0]['date']
    dateLabel=Label(window,text='Forcast for : '+date+' ',font=("Helvetica",12))
    dateLabel.place(x=10,y=160)
    
    tempc=data['data']['current_condition'][0]['temp_C']
    tempf=data['data']['current_condition'][0]['temp_F']
    tempcLabel=Label(window,text='Temperature : '+tempc+' *C  '+tempf+' *F',font=("Helvetica",12))
    tempcLabel.place(x=10,y=200)
    
    windspeedmiles=data['data']['current_condition'][0]['windspeedMiles']
    windspeedkmph=data['data']['current_condition'][0]['windspeedKmph']
    windspeedLabel=Label(window,text='WindSpeed  :  '+windspeedmiles+' miles  '+windspeedkmph+' kmph',font=("Helvetica",12))
    windspeedLabel.place(x=10,y=220)
    
    humidity=data['data']['current_condition'][0]['humidity']
    humidityLabel=Label(window,text='Humidity   : '+humidity+'',font=("Helvetica",12))
    humidityLabel.place(x=10,y=260)
    
    visibility=data['data']['current_condition'][0]['visibility']
    visibilityLabel=Label(window,text='Visibility    : '+visibility+' feet',font=("Helvetica",12))
    visibilityLabel.place(x=10,y=280)
    
    pressure=data['data']['current_condition'][0]['pressure']
    pressureLabel=Label(window,text='Pressure   : '+pressure+' pascals',font=("Helvetica",12))
    pressureLabel.place(x=10,y=300)
    
    sunrise=data['data']['weather'][0]['astronomy'][0]['sunrise']
    sunriseLabel=Label(window,text='Sunrise  :  '+sunrise+'',font=("Helvetica",12))
    sunriseLabel.place(x=10,y=340)
    
    sunset=data['data']['weather'][0]['astronomy'][0]['sunset']
    sunsetLabel=Label(window,text='Sunset   :  '+sunset+'',font=("Helvetica",12))
    sunsetLabel.place(x=10,y=360)
    
    moonrise=data['data']['weather'][0]['astronomy'][0]['moonrise']
    moonriseLabel=Label(window,text='Moonrise  :  '+moonrise+'',font=("Helvetica",12))
    moonriseLabel.place(x=10,y=400)


#3


def findweather(cityEntry):
    if (str(cityEntry.get())=='' or not str(cityEntry.get())):
        message="Enter Valid City"
        heading="Empty Fields"
        messagebox.showinfo(heading,message)
    else:
        readweather(str(cityEntry.get()))



#4
## Load Image from Url
#image_url = "https://raw.githubusercontent.com/mohit-malik1/WeatherPy/master/w5.png"
#image_byt = urlopen(image_url).read()
#image_b64 = base64.encodebytes(image_byt)




#5
window=Tk()
window.title('Weather Channel')
window.geometry("500x500+450+150")
photo=PhotoImage(file="giphy.gif")
#photo=PhotoImage(data=image_b64)
BL=Label(window,image=photo)
BL.place(x=200,y=40)
weatherLabel=Label(window,text='Weather Channel',font=("Helvetica",20,"bold"))
weatherLabel.place(x=130,y=0)
cityLabel=Label(window,text='City : ',font=("Helvetica",15,"bold"))
cityLabel.place(x=10,y=60)
cityEntry=Entry(window,bd=3)
cityEntry.place(x=70,y=65)
L4=Label(window,text="Made by : Mohit Malik",font=("Helvetica",14,"bold"))
L4.place(x=130,y=440)
B1=Button(window,text="Submit",command=lambda: findweather(cityEntry),bd=5,width=18,height=1)
B1.place(x=40,y=100)

window.mainloop()

