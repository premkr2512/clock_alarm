from playsound import playsound
from tkinter import *
from win10toast import ToastNotifier
import datetime
import time
from plyer import notification
import pyttsx3 as p
import smtplib
from Adafruit_IO import Client, Feed, RequestError
ADAFRUIT_IO_KEY = 'aio_nbJJ32IGEx9gySFQn3DXQozPfd56'
ADAFRUIT_IO_USERNAME = 'Prem2512'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
engine = p.init("sapi5")
voice = engine.getProperty("voices")
#sender = "premsherghati"
#rec = "premsheghati@gmail.com"
#sender_pass = input(str("enter ur passward "))
#message = "Hi abhishek bete"
#server = smtplib.SMTP("smtp.gmail.com",587)
#server.starttls()
#server.login(sender,sender_pass)
#print("login successfully")
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def show():
    top = Toplevel()
    level = Label(top,text = "Clock",font = "ariel 60")
    level.grid(row = 2, column = 0 )
    level = Label(top,text = "Alarm Set",font = "ariel 60")
    level.grid(row = 0, column = 0)


    L = Label(top,font = "ariel 80",bg = "black", fg ="red")
    L.grid(row = 2,column =2,padx = 100,pady= 100)
    L1 = Label(top,text = "Hour         Min         Sec",font = "ariel 40")
    L1.grid(row = 3,column = 2)


    def start():
        global Time
    Time = time.strftime("%H:%M:%S  %p")
    L['text'] = Time
    L.after(1000,start)

    start()




def alarm(set_alarm):
    toast = ToastNotifier()
    digital = aio.feeds('btn')
    while True:
        time.sleep(1)
        date = datetime.datetime.now()
        now = date.strftime("%H:%M:%S")
        print(now)
        if now == set_alarm:
            print("alarm Clock")


            notification.notify(title = " wake up",message = "Early to wake early to Make a man healthy wealthy and wise"
                                ,app_icon = "C:\\Users\\welcome\\IdeaProjects\\game1\\glass.ico",timeout = 10)
            toast.show_toast("Alarm Clock",duration= 1)


            speak("wake sir its your time")

            aio.send("btn","ON")
            data = aio.receive(digital.key)
            if str(data.value) == "ON":
                print('received <- ON\n')
            elif str(data.value) == "OFF":
                print('received <- OFF\n')
                time.sleep(0.5)


            playsound("C:\\Users\\welcome\\IdeaProjects\\game1\\Extreme - AShamaluevMusic.mp3")


            #server.sendmail(sender,rec,massage)
            #print("sent successfully")

def get_value():
    set_alarm = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm)

root = Tk()
root.geometry("500x250")
info = Label(root,text ="Clock",font = "ariel 60", fg = "blue").grid(row= 0 , column= 2)
set_time = Label(root,text= "set_alarm",font = "ariel 30", fg = "blue").grid(row = 1,column = 0)
hour = StringVar()
min = StringVar()
sec = StringVar()

hour_e= Entry(root, textvariable= hour,bg= "grey",width = 4).grid(row = 1,column = 1)
min_e =Entry(root, textvariable= min,bg ="grey",width = 4).grid(row = 1,column = 2)
sec_e =Entry(root, textvariable= sec,bg ="grey",width = 4).grid(row = 1,column = 3)

submit = Button(root, text = "set_alarm",font = "ariel 10",width = 10,command =get_value).place(x = 100 ,y =150)
clock = Button(root , text = "Show_clock",font = "ariel 10", width= 10, command =show ).place(x = 250,y = 150)
root.mainloop()
