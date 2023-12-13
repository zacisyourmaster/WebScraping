from bs4 import BeautifulSoup
import requests

import sys
import datetime
import smtplib, ssl

sys.stdout.reconfigure(encoding="utf-8")
url = "https://www.basketball-reference.com/boxscores/"
result = requests.get(url).text
soup = BeautifulSoup(result, "html.parser")
cal = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

game_list = soup.find_all("div", class_="game_summary")
scores = []
for game in game_list:
    loser = game.find("tr", class_="loser").text.strip()
    winner = game.find("tr", class_="winner").text.strip()
    lInfo = loser.split("\n")
    wInfo = winner.split("\n")
    scores.append(
        wInfo[0] + " defeated " + lInfo[0] + " " + wInfo[1] + " to " + lInfo[1]
    )

with open("scores.txt", "w") as f:
    f.write(
        "Hi Zach!\nIn total there were "
        + str(len(scores))
        + " games today. Let's cover them all\n"
    )
    for score in scores:
        f.write(score + "\n")


def sendEmail():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = ""  # Enter your address
    receiver_email = "zac15590@gmail.com"  # Enter receiver address
    # password = input("Type your password and press enter: ")
    password = ""
    with open("scores.txt", "r") as f:
        message = f.read()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


h1 = soup.find("h1").string
date = h1


def checkDate():
    today = str(datetime.datetime.today())
    iMonth = int(today[5:7])
    day = int(today[8:10])


sendEmail()

# import os
# from selenium import webdriver

# os.environ['PATH']+=r"C:/SeleniumDrivers"
# driver=webdriver.Chrome()
# driver.get(url)
