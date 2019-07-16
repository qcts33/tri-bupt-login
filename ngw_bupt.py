import json

import PySimpleGUI as sg
import requests
from bs4 import BeautifulSoup
import click


def _login(auth):
    login_url = "http://ngw.bupt.edu.cn/login"
    res = requests.post(login_url, auth)
    soup = BeautifulSoup(res.text, "lxml")
    try:
        result = soup.find("h3").text
    except AttributeError:
        result = soup.find("div", {"class": "ui error message"}).text
    return result.strip()


@click.group()
def main():
    pass


@main.command("list")
def list_names():
    for name in data.keys():
        click.echo(name)


@main.command()
def logout():
    requests.get("http://ngw.bupt.edu.cn/logout")
    click.echo("logout")


@main.command()
@click.argument("name", default="")
def login(name):
    # data = load_data()
    if len(name) == 0:
        name = next(iter(data.keys()))
    if name in data:
        click.echo(f"Auth with {name}")
        result = _login(data[name])
        click.echo(result)
    else:
        click.echo("no such config")


@main.command()
def gui():
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
            result = _login(auth)
            window.Element("_Output_").Update(result)
        if event == "Logout":
            requests.get("http://ngw.bupt.edu.cn/logout")
            window.Element("_Output_").Update("已登出")


if __name__ == "__main__":
    with open("bupt_login.json", "r") as fp:
        data = json.load(fp)
    main()
