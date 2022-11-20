from  tkinter import *
from cryptography.fernet import Fernet
import os
import requests
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk
import ctypes.wintypes
CSIDL_PERSONAL = 5       # My Documents
SHGFP_TYPE_CURRENT = 0   # Get current, not default value

buf= ctypes.create_unicode_buffer(ctypes.wintypes.MAX_PATH)
ctypes.windll.shell32.SHGetFolderPathW(None, CSIDL_PERSONAL, None, SHGFP_TYPE_CURRENT, buf)

#print(buf.value)
# 200 login sucess
# 404 servererror
# 303 wrong id or password
# 300 already connected
# 100 loggedout
# 101 logout unsucessful
# 505 error not connected to gla or modify application

def f_logout():
    try:
        r = requests.get(url = 'http://172.16.10.20:1000/logout?'+data)
        global kl
        kl = False
        return 100;
    except:
        return 101;
       
def  f_login(uname,upass):
  global data
  try:
    r = requests.get(url = 'http://www.gstatic.com/generate_204')
    data = (r.text)
    if data == '':
        print('Internet is already connected!')
        return 300; 
    else:
        data=data.split('?')[1]
        data=data.split('"')[0]
        r = requests.get(url = 'http://172.16.10.20:1000/fgtauth?'+data)
        stat={
            '4Tredir':'http%3A%2F%2Fwww.gstatic.com%2Fgenerate_204',
            'magic':data,
            'username':uname,
            'password':upass
        }
        a = requests.post(url = 'http://172.16.10.20:1000', data = stat)
        data2 = (a.text)
        keepalive = data2.split('?')[1]
        keepalive = keepalive.split('"')[0]
        if 'keepalive' in data2:
            kl = True
            def update():
                try:
                    r = requests.get(url = 'http://172.16.10.20:1000/keepalive?'+keepalive)
                    if kl == True: window.after(500000, update)
                    #refresh = Label(window, text = 'Refreshed!')
                    #refresh.pack()
                    return 11;
                except:
                    return 12;
            if kl == True: window.after(500000, update)
            print('login successful')
            return 200;
            
        else:
            print('wrong id pass')
            return 303;
  except:
        return 505
            





















window=Tk()
window.geometry("320x420")

user_id=""
user_pass=""


def read_data(r_data):
        
        if r_data!="":
            id=r_data.split("_i_hate_attendance_")[0]
            password=r_data.split("_i_hate_attendance_")[1]
            id=decstr(id)
            password=decstr(password)
            global user_id
            global user_pass
            user_id=id
            user_pass=password
   


def encstr(str):
    fernet =Fernet(b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg=')
    encid=fernet.encrypt(str.encode())
    return encid


def decstr(str):
    fernet =Fernet(b'ZmDfcTF7_60GrrY167zsiPd67pEvs0aGOv2oasOM1Pg=')
    decid=fernet.decrypt(str).decode()
    return decid




def main():
    def saveid():
        id=e1.get()
        password=e2.get()
        if( validate(id,password) ):
            f=open(buf.value+'abc.fortinet','w')
            enccoded_id=encstr(id).decode()
            encoded_pass=encstr(password).decode()
            save_token=enccoded_id+"_i_hate_attendance_"+encoded_pass
            f.write( save_token )
            f.close()
            f=open(buf.value+'abc.fortinet','r')
            read_data(f.read())
            f.close()
            openconn()

    def validate(str1,str2):
        if str1=="" or str2=="" :
            strr.set("No parameter can be empty")
            return False
        return True

    f1=Frame()
    l1=Label(f1,text="Login once")
    l1.pack()
    f1.place(x=0,y=0,width=320,height=420)
    l2=Label(f1,text="Fortinet Login Id")
    l2.pack()
    e1=Entry(f1)
    e1.pack(pady=20)
    l3=Label(f1,text="Fortinet password")
    l3.pack()
    e2=Entry(f1)
    e2.pack(pady=20)
    bs=Button(f1,text="save and connect",command=saveid)
    bs.pack()
    strr=StringVar()
    l_message=Label(f1,textvariable=strr)
    l_message.pack()
          
def addunap():
    def validate(str1,str2):
        if str1=="" or str2=="" :
            strr.set("No parameter can be empty")
            return False
        return True
    def saveid():
        id=e1.get()
        password=e2.get()
        if( validate(id,password) ):
            f=open(buf.value+'abc.fortinet','w')
            enccoded_id=encstr(id).decode()
            encoded_pass=encstr(password).decode()
            save_token=enccoded_id+"_i_hate_attendance_"+encoded_pass
            f.write( save_token )
            f.close()
            f=open(buf.value+'abc.fortinet','r')
            read_data(f.read())
            f.close()
            strr.set("Sucessfully changed Password ! ")

    f4=Frame()
    f4.place(x=40,y=120,width=250,height=250)

    l1=Label(f4,text="Change Fortinet ID and Password")
    l2=Label(f4,text="Fortinet id")
    e1=Entry(f4)
    l3=Label(f4,text="Fortinet password")
    e2=Entry(f4)
    bs=Button(f4,text="Save",command=saveid)
    strr=StringVar()
    l_m=Label(f4,textvariable=strr,pady=5)
    l1.pack(pady=5)
    l2.pack()
    e1.pack(pady=10)
    l3.pack()
    e2.pack(pady=10)
    bs.pack()
    l_m.pack()
def info():
    f4=Frame()
    f4.place(x=40,y=120,width=250,height=250)
    l1=Label(f4,text="How to use Fortilog")
    l1.pack()


def setting():
    f2=Frame()
    f2.configure(bg="black")
    button_back=Button(f2,text="back",command=openconn)
    button_back.place(x=7,y=390)
    f2.place(x=0,y=0,width=320,height=420)
    b1=Button(f2,text="change fortinet ID and Password",width=50,command=addunap)
    b2=Button(f2,text="contribute to out patreon",width=50)
    b3=Button(f2,text="How to use fortilog? ",width=50,command=info)
    b4=Button(f2,text="contact us",width=50)
    b1.pack()
    b2.pack()
    b3.pack()
    b4.pack()

def openconn():
    if user_id=="":
        f=open(buf.value+'abc.fortinet','r')
        read_data(f.read())
        f.close()

    user_id_w="Welcome , "+user_id
    def login():
        res=f_login(user_id,user_pass)
        if(res==200):
            con_stat.set("Connected sucessfully")
            b1.configure(state=DISABLED)
            b3.pack()
        elif res==300:
            message_conn.set("Either you are not connected to GLA WIFI \n or \n You are already Logged In")
        elif res==505:
            message_conn.set("Not Connected to WIFI")  
        elif res==303:
            message_conn.set("Wrong ID or Password")         
    def logout():
        if(f_logout()==100):
            b3.pack_forget()
            con_stat.set("Connect")
            b1.configure(state=NORMAL)
        else:
            message_conn.set("Error logging out! restart Application")    

    f3=Frame()
    f3.place(x=0,y=0,width=320,height=420)
    l1=Label(f3,text=user_id_w,font='Arial 14 bold',pady=20)
    l_in=Label(f3,pady=30)
    ll=Label(f3)
    b3=Button(f3,text="Logout",command=logout,padx=30,pady=10)
    con_stat=StringVar()
    con_stat.set("Connect")
    b1=Button(f3,textvariable=con_stat,padx=30,pady=10,command=login)
    b2=Button(f3,text="settings",command=setting,padx=30,pady=10)
    message_conn=StringVar()
    
    l2=Label(f3,textvariable=message_conn,pady=10)
    
    l1.pack()
    l_in.pack()
    b1.pack()
    ll.pack()
    b2.pack()
    l2.pack()



if os.path.exists(buf.value+'abc.fortinet'):
    file=open(buf.value+'abc.fortinet','r')
    x=file.read()
    if x=="":
        main()
    else :
        openconn()
else:
    main()

# b1=Button( text="change frame",command=main )
# b2=Button(text="setting",command=setting)
# b1.pack()
# b2.pack()
window.resizable(0,0)
window.title("Fortilog alpha1")
icon =PhotoImage(file='icon.png')
window.iconphoto(True,icon)

#  trying to make it come in system tray
def quit_window(icon, item):
       icon.stop()
       window.destroy()

# Define a function to show the window again
def show_window(icon, item):
   icon.stop()
   window.after(0,window.deiconify())

# Hide the window and show on the system taskbar
def hide_window():
   window.withdraw()
   image=Image.open("icon.png")
   menu=(item('Quit', quit_window), item('Show', show_window))
   icon=pystray.Icon("name", image, "My System Tray Icon", menu)
   icon.run()

window.protocol('WM_DELETE_WINDOW', hide_window)
window.mainloop()
