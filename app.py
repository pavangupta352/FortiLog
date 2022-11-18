import requests
import time
from tkinter import *

root = Tk()
lab = Label(root)
lab.pack()
def loginnow():
    #uname = 'pavangupta_cs20'
    #upass = 'GLA#t45sd8'
    r = requests.get(url = 'http://www.gstatic.com/generate_204')
    global data 
    data = (r.text)
    if data == '':
        myLabel = Label(root, text = "Internet is already connected!")
        myLabel.pack()
    else:
        data=data.split('?')[1]
        data=data.split('"')[0]
        r = requests.get(url = 'http://172.16.10.20:1000/fgtauth?'+data)
        stat={
        '4Tredir':'http%3A%2F%2Fwww.gstatic.com%2Fgenerate_204',
        'magic':data,
        'username':'pavangupta_cs20',
        'password':'GLA#t45sd8'
        }
        r = requests.post(url = 'http://172.16.10.20:1000', data = stat)
        data2 = (r.text)
        keepalive = data2.split('?')[1]
        keepalive = keepalive.split('"')[0]
        if 'keepalive' in data2:
            myLabel1 = Label(root, text = "login successful")
            myLabel1.pack()
            def update():
               r = requests.get(url = 'http://172.16.10.20:1000/keepalive?'+keepalive)
               root.after(500000, update)
               refresh = Label(root, text = 'Refreshed!')
               refresh.pack()
            root.after(500000, update)
        else:
            myLabel3 = Label(root, text = "wrong id pass")
            myLabel3.pack()

def logoutnow():
    r = requests.get(url = 'http://172.16.10.20:1000/logout?'+data) 
    myLabel1 = Label(root, text = "logout successful")
    myLabel1.pack()
    root.destroy()

myButton = Button(root, text="Connect! ", command=loginnow)
myButton.pack()
myButton2 = Button(root, text="Disconnect! and close the program ", command=logoutnow)
myButton2.pack()

root.mainloop()
