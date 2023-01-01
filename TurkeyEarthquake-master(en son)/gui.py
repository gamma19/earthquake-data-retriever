from tkinter.messagebox import *
import tkinter
from tkinter import *
import os
import re
import json
from datetime import date


window = Tk() #instantiate an instance of a window
# create listbox object
listbox = Listbox(window, height=16,
                  width=50,
                  bg="grey",
                  activestyle='dotbox',
                  font="Helvetica",
                  fg="yellow",
                  selectmode='single')



listbox2 = Listbox(window, height=15,
                  width=20,
                  bg="yellow",
                  activestyle='dotbox',
                  font="Helvetica",
                  fg="red",
                  )

listbox3 = Listbox(window, height=15,
                  width=30,
                  bg="purple",
                  activestyle='dotbox',
                  font="Helvetica",
                  fg="white",
                  )

# Define the size of the window.
window.geometry("300x500")
window.resizable(0, 0)

# pack the widgets
listbox.pack()
listbox.place(x=35,y=150)

listbox2.pack()
listbox2.place(x=660,y=150)

listbox3.pack()
listbox3.place(x=960,y=150)

photo= PhotoImage(file='images\photo.png')
window.geometry("1300x650")
window.title("Earthquake Danger Calculator")

icon = PhotoImage(file='images\logo.png')
window.iconphoto(True,icon)
window.config(background="#f5eece")

label1 = Label(window,
              text="Cities,Their Danger Index and Weather Condition ",
              font=('Arial', 35,'bold'),
              fg='yellow',
              bg='black',
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20)


label1.place(x=70, y=30)
#label2.place(x=85, y=155)

counter = 0

def run():
    os.system('rQuake.py')
    path = 'data\\quakes.txt'
    # Check whether the specified
    # path exists or not
    isExist = os.path.exists(path)
    print(isExist)
    if (isExist == False):
        tkinter.messagebox.showinfo(title="Alert!", message="Data not found!")
    elif (isExist == True):
        tkinter.messagebox.showinfo(title="Success!", message="Data has been acquired!")



buttonGetData = Button(window,
                       text="Get Data",
                       command=run,
                       font=("Comic Sans", 20),
                       fg="#00FF00",
                       bg="black",
                       activeforeground="#00FF00",
                       activebackground="black",)  #If you want to disable button use state="DISABLED"


def listCities():
    os.system('csv_to_json.py')
    os.system('processing.py')
    resultPath = 'data\\result.txt'
    # Check whether the specified
    # path exists or not
    isExistResult = os.path.exists(resultPath)
    print(isExistResult)
    if (isExistResult == False):
        tkinter.messagebox.showinfo(title="Alert!", message="Result couldn't be created!")
    elif (isExistResult == True):
        tkinter.messagebox.showinfo(title="Success!", message="Result has been successfully created!")
        try:
            file = open("data\\result.txt")
            for line in range(0,16):
                listbox.insert(line, file.readline())
        except:
            pass
    window.update_idletasks()


buttonList = Button(window,
                text="List Cities",
                command=listCities,
                font=("Comic Sans",20),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",)  #If you want to disable button use state="DISABLED"

#plus = PhotoImage(file="C:\\Users\\gamma3\\Desktop\\SOFTWARE ENGINEERING\\TurkeyEarthquakeDataCrawler-master\\images\\plus.png")
date=tkinter.StringVar()
date2=tkinter.StringVar()

date_label = tkinter.Label(window, text='Date(YYYY-MM-DD)', font=('calibre', 10, 'bold'))
date_entry = tkinter.Entry(window, textvariable=date, font=('calibre', 10, 'normal'))

date2_label = tkinter.Label(window, text='Date(YYYY.MM.DD)', font=('calibre', 10, 'bold'))
date2_entry = tkinter.Entry(window, textvariable=date2, font=('calibre', 10, 'normal'))

# open and load your user.json file

name=tkinter.StringVar()
name2=tkinter.StringVar()


# creating a label for
# name using widget Label
name_label = tkinter.Label(window, text='City Name(Case and Turkish character sensitive)', font=('calibre', 10, 'bold'))
name2_label = tkinter.Label(window, text='City Name(All capital English characters)', font=('calibre', 10, 'bold'))
# creating a entry for input
# name using widget Entry
name_entry = tkinter.Entry(window, textvariable=name, font=('calibre', 10, 'normal'))
name2_entry = tkinter.Entry(window, textvariable=name2, font=('calibre', 10, 'normal'))


name_label.place(x=430, y=540)
name2_label.place(x=890, y=540)

name_entry.place(x=740, y=540)
name2_entry.place(x=1150, y=540)

date_label.place(x=610, y=515)
date_entry.place(x=740, y=515)

date2_label.place(x=1025, y=515)
date2_entry.place(x=1150, y=515)

#=======================USE THIS FOR LISTING ALL CITIES=========================

def queryWeather():
    listbox2.delete(0, END)
    with open('weather_old\\{}.json'.format(date.get()), 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        for i in reversed(range(0, 80)):
            try:
                j = data['{}'.format(i)]
                ans1 = j['City']
                ans2 = j['Temp']
                ans3 = j['Condition']
                ans4 = j['Humidity']
                print(ans1)
                # ans = "\n" + "City: " + ans1 + " \n" + "Temp: " + ans2 + " \n" + "Condition: " + ans3 + "\n" + "Humidity: " + ans4 + "\n"
                if name.get() == ans1:
                    listbox2.insert(1, "City: " + ans1)
                    listbox2.insert(2, "Temp: " + ans2 + "°C")
                    listbox2.insert(3, "Condition: " + ans3)
                    listbox2.insert(4, "Humidity: " + "%" + ans4)
            except TypeError as e:
                print(f"data: {data}, exception: {str(e)}")

buttonQueryWeather = Button(window,
                       text="Query Weather",
                       command=queryWeather,
                       font=("Comic Sans", 20),
                       fg="#00FF00",
                       bg="black",
                       activeforeground="#00FF00",
                       activebackground="black",)  #If you want to disable button use state="DISABLED"

def queryQuake():
    listbox3.delete(0, END)
    with open('quakes_raw.json', 'r', encoding='utf-8') as json_file2:
        quake = json.loads(json_file2.read())
        for p in quake:
            try:
                m = quake['{}'.format(p)]
                ans11 = m['Date']
                ans22 = m['Time']
                ans33 = m['Latit(N)']
                ans44 = m['Long(E)']
                ans55 = m['Depth(km)']
                ans66 = m['Magnitude']
                ans77 = re.search(r'\(([^)]+)', m['Region']).group(1)
                #ans77 = m['Region']
                print(ans77)

                # ans = "\n" + "City: " + ans1 + " \n" + "Temp: " + ans2 + " \n" + "Condition: " + ans3 + "\n" + "Humidity: " + ans4 + "\n"
                if (name2.get() == ans77 and date2.get() == ans11):
                    listbox3.insert(0, "Date: " + ans11)
                    listbox3.insert(1, "Time: " + ans22)
                    listbox3.insert(2, "Latit(N): " + ans33)
                    listbox3.insert(3, "Long(E): " + ans44)
                    listbox3.insert(4, "Depth(km): " + ans55)
                    listbox3.insert(5, "Magnitude: " + ans66)
                    listbox3.insert(6, "Region: " + ans77)
                    listbox3.insert(7, " ")
            except:
                #print(f"data: {quake}, exception: {str(w)}")
                pass

def getWeather():
    os.system('weather.py')
    window.update_idletasks()

buttonQueryCities = Button(window,
                       text="Query Cities",
                       command=queryQuake,
                       font=("Comic Sans", 20),
                       fg="#00FF00",
                       bg="black",
                       activeforeground="#00FF00",
                       activebackground="black",)  #If you want to disable button use state="DISABLED"

buttonGetWeather= Button(window,
                       text="Get Weather",
                       command=getWeather,
                       font=("Comic Sans", 20),
                       fg="#00FF00",
                       bg="black",
                       activeforeground="#00FF00",
                       activebackground="black",)  #If you want to disable button use state="DISABLED"

buttonGetData.place(x=35, y=580)
buttonList.place(x=200, y=580) #We can also use .pack()
buttonGetWeather.place(x=350, y=580)
buttonQueryWeather.place(x=667, y=580)
buttonQueryCities.place(x=1050, y=580)

print()

window.mainloop() #placing window on computer screen, listen for events