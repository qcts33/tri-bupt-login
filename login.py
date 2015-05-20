#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import sys
import re
import locale
import getpass

s = requests.Session()
username = ''
password = ''

def get_string(Msg, msga):
    msg = locale.atoi(Msg)
    if (msg == 0 or msg == 1):
        if (msg == 1 and msg != ''):
            if (msga == 'error0'):
                print('The IP does not allow Web-log')
                return False
            elif (msga == 'error1'):
                print('The account does not allow Web-log')
                return False
            elif (msga == 'error2'):
                print('This account does not allow change password')
                return False
            elif (msga == 'ldap auth error'):
                print('Ivalid account or password, please login again')
                return False
            else:
                print(msga)
                return False
        else:
            print('Ivalid account or password, please login again')
            return False
    elif (msg == 2):
        print('This account now is using on other computer, please logout first!')
        return False
    elif (msg == 3):
        print('This account can be used on the appointed address only.')
        return False
    elif (msg == 4):
        print('This account overspent or over time limit')
        return False
    elif (msg == 5):
        print('This account has been suspended')
        return False
    elif (msg == 6):
        print('System buffer full')
        return False
    elif (msg == 8):
        print('This account is in use. Unable to change')
        return False
    elif (msg == 7):
        print('???')
        return False
    elif (msg == 9):
        print('New password and confirmation do not match. Unable to change')
        return False
    elif (msg == 10):
        print('Password Changed Successfully')
        return False
    elif (msg == 11):
        print('This account can be used on the appointed address only')
        return False
    elif (msg == 14):
        print('Logout successfully')
        return False
    elif (msg == 15):
        return True
    else:
        return True


def get_login(url):
    print("username: " + username)
    print("password: xxxxx" + password)
    payload = {'DDDDD': username, 'upass': password, 'savePWD': 0, '0MKKey': ''}
    r = s.post(url, data = payload)
    Msg = re.findall(r'Msg=(\d{2})', r.text)
    msga = re.findall(r'msga=\'(.+)\'', r.text)
    if (Msg and msga):
        return get_string(Msg[0], msga[0])
    else:
        return True


def get_server():
    request_server = "http://www.baidu.com/"
    r = s.get(request_server)
    authentication_server = r.request.url
    if (authentication_server == request_server):
        print('您已登陆！')
        return ''

    print("Authentication server url: " + authentication_server)
    return authentication_server

def validate_parameter():
    if (len(sys.argv) != 3 and len(sys.argv) != 2):
        parameter_error()
        return False
    if (sys.argv[1] != 'in' and sys.argv[1] != 'out'):
        parameter_error()
        return False
    if (sys.argv[1] == 'in' and len(sys.argv) != 3):
        parameter_error()
        return False
    if (sys.argv[1] == 'out' and len(sys.argv) != 2):
        parameter_error()
        return False

    return True

def parameter_error():
    print('Usage:')
    print(sys.argv[0] + ' [in|out] [username]')

if __name__ == '__main__':
    print('Start login...')
    if (not validate_parameter()):
        sys.exit(-1)

    if (sys.argv[1] == 'in'):
        username = sys.argv[2]
        password = getpass.getpass('Password: ')

        server_url = get_server()
        if (server_url == ''):
            sys.exit(0)

        if (get_login(server_url)):
           print('Login successfully')

    else:
        r = s.get('http://gw.bupt.edu.cn/F.htm')
        print('Logout successfully')


