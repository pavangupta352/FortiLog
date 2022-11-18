import requests
import os
import time


#uname = ''
#upass = ''
#if uname != '' and upass != '':
uname = input('Enter username\n')
upass = input('Enter password\n')

r = requests.get(url = 'http://www.gstatic.com/generate_204')
data = (r.text)
if data == '':
    print('Internet is already connected!')
    k=input("press any key to exit") 
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
    r = requests.post(url = 'http://172.16.10.20:1000', data = stat)
    data2 = (r.text)
    if 'keepalive' in data2:
        print('login successful')
        kk=input("press any key to logout and exit")
        r = requests.get(url = 'http://172.16.10.20:1000/logout?'+data)   
    else:
        print('wrong id pass')
        kk=input("press any key to exit") 
    