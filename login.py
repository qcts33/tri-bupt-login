#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, os, sys, re, locale, getpass, json

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
    print("password: *********")
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
    if (len(sys.argv) > 3):
        return False
    if (len(sys.argv) == 2 and not (sys.argv[1] == 'in' or sys.argv[1] == 'out')):
        parameter_error()
        return False

    return True


def parameter_error():
    print('Usage:' + sys.argv[0] + ' [in|out] ' + '[Profile]')


def login_without_config_file():
    username = input("Username: ")
    password = getpass.getpass('Password: ')


def login_with_config_file(config_file):
    with open(config_file) as tmp_file:
        tmp = json.load(tmp_file)["Applications"]
        if "tri-bupt-login" in tmp:
            profile_list = tmp["tri-bupt-login"];

            if len(sys.argv) == 3:
                if sys.argv[2] in profile_list:
                    profile = profile_list[sys.argv[2]]
                else:
                    print ("Can't fine the '" + sys.argv[2] + "' profile")
                    return ()
            if (len(sys.argv) < 3):
                profile = profile_list["default"]
        else:
            print ('Can not find "tri-bupt-login" field in your'
                    'configuration file!')
            return ()

        print (profile)
        return (profile['username'], profile['password'])


def get_pass():
    config_file_path = ['~/.tri_bupt_login.json',
                         '~/.dot/tri_config.json']

    for cur_config_file in config_file_path:
        config_file_full_path = os.path.expanduser(cur_config_file)
        if (os.path.exists(config_file_full_path) is True):
            config_file = config_file_full_path
            t = login_with_config_file(config_file)
            if (len(t) != 0):
                return t;
            else:
                return login_without_config_file();
            break;
    else:
        return login_without_config_file();



if __name__ == '__main__':
    if (not validate_parameter()):
        sys.exit(-1)

    if (len(sys.argv) == 1 or sys.argv[1] == 'in'):
        print('Start login...')
        u_and_pass = get_pass()
        username = u_and_pass[0]
        password = u_and_pass[1]

        server_url = get_server()
        if (server_url == ''):
            sys.exit(0)

        if (get_login(server_url)):
           print('Process finished')

    else:
        r = s.get('http://gw.bupt.edu.cn/F.htm')
        print('Logout successfully')


