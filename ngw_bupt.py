import requests
import json
from bs4 import BeautifulSoup
import PySimpleGUI as sg


def login(auth):
    login_url = "http://ngw.bupt.edu.cn/login"
    res = requests.post(login_url, auth)
    soup = BeautifulSoup(res.text, "lxml")
    try:
        result = soup.find("h3").text
    except AttributeError:
        result = soup.find("div", {"class": "ui error message"}).text
    return result.strip()


def gui():
    with open("bupt_login.json", "r") as fp:
        data = json.load(fp)
    layout = [
        [sg.Text("Please Select the auth info")],
        [sg.InputCombo(tuple(data.keys()), size=(20, 1))],
        [sg.Text("", key="_Output_", size=(20, 1))],
        [sg.Button("Login"), sg.Button("Logout")],
    ]
    window = sg.Window("Login", layout)
    while True:
        event, values = window.Read()
        if event is None:
            break
        if event == "Login":
            name = values[0]
            auth = data[name]
            result = login(auth)
            window.Element("_Output_").Update(result)
        if event == "Logout":
            requests.get("http://ngw.bupt.edu.cn/logout")
            window.Element("_Output_").Update("已登出")


if __name__ == "__main__":
    gui()
