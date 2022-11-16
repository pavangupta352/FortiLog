from os import path, popen, remove
from time import sleep
from requests import post, head, Session, ConnectionError
from getpass import getpass
from bs4 import BeautifulSoup
import sys
import hashlib

def login(uname, passw):
    url_1 = 'http://www.google.co.in'

    headers = \
        {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

    session = Session()

   # res = session.get(url_1, headers=headers)

    #magic = res.url.split('?')[1]

   # my_referer = res.url
    soup = BeautifulSoup(request.get('http://google.com').text , "html.parser")

    magic = soup.find("input", {'name': "magic"}).attrs['value']
    Tredir = soup.find("input", {'name': "4Tredir"}).attrs['value']

    payload = {
        '4Tredir': Tredir,
        'magic': str(magic),
        'username': uname,
        'password': passw,
        }

    url_2 = 'http://172.16.10.20:1000/'

    res = post(url_2, headers=headers, data=payload)

    if 'Failed' in res.text:
        return False
    else:
        print('Successfully authenticated....!')
        return True


def main():
   # str = sys.argv[2]
  #  print("Checking for user : " + sys.argv[1] + ", password : " + hashlib.md5(str.encode()).hexdigest() )
    try:
        res = head('http://www.google.co.in')
        print('Already connected, pinged ' + res.url + ' status : ' + repr(res.status_code))
	# for att in dir(res):
            # print (att, getattr(res, att))
    except ConnectionError:
            username = 'pavangupta_cs20'
            password = 'GLA#t45sd8'

            if login(username, password):
               print('Login successfull.....!\n')

            else:
                print('Login Error. Try again......!\n')

if __name__ == '__main__':
    main()
