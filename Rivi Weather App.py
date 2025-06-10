from tkinter import *
from tkinter import ttk
import requests


def data_get():
    city = city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=746c1cfdecb7d39f3ff407d1e3766661").json()
    w_label1.config(text=data["weather"][0]["main"])
    wb_label1.config(text=data["weather"][0]["description"])
    temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))
    pre_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Rivi Weather")
win.config(bg ="sky blue")
win.geometry("500x570")

name_label = Label(win,text="Rivi Weather App",font=(30))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Andhra Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox(win,text="Rivi Weather App",values=list_name,font=(20),textvariable=city_name)
com.place(x=25,y=120,height=50,width=450)


w_label = Label(win,text="Weather Climate",font=(20))

w_label.place(x=25,y=260,height=50,width=210)

w_label1 = Label(win,text=" ",font=(20))

w_label1.place(x=250,y=260,height=50,width=210)




wb_label = Label(win,text="Weather Description",font=(17))

wb_label.place(x=25,y=330,height=50,width=210)

wb_label1 = Label(win,text=" ",font=(17))

wb_label1.place(x=250,y=330,height=50,width=210)



temp_label = Label(win,text="Temperature",font=(20))

temp_label.place(x=25,y=400,height=50,width=210)

temp_label1 = Label(win,text=" ",font=(20))

temp_label1.place(x=250,y=400,height=50,width=210)



pre_label = Label(win,text="Pressure",font=(20))

pre_label.place(x=25,y=470,height=50,width=210)

pre_label1 = Label(win,text=" ",font=(20))

pre_label1.place(x=250,y=470,height=50,width=210)


done_button = Button(win,text="Done",font=(20),command=data_get)
done_button.place(y=190,height=50,width=100,x=200)





win.mainloop()