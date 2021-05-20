# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 11:23:08 2021

@author: franc
"""
import json
import re
import os
import sys
import progressbar
import time
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

def art():
    print("          _____                    _____                    _____                    _____                _____       \n         /\\    \\                  /\\    \\                  /\\    \\                  /\\    \\              |\\    \\         \n        /::\\    \\                /::\\    \\                /::\\    \\                /::\\    \\             |:\\____\\        \n       /::::\\    \\              /::::\\    \\              /::::\\    \\              /::::\\    \\            |::|   |        \n      /::::::\\    \\            /::::::\\    \\            /::::::\\    \\            /::::::\\    \\           |::|   |        \n     /:::/\\:::\\    \\          /:::/\\:::\\    \\          /:::/\\:::\\    \\          /:::/\\:::\\    \\          |::|   |        \n    /:::/__\\:::\\    \\        /:::/__\\:::\\    \\        /:::/__\\:::\\    \\        /:::/  \\:::\\    \\         |::|   |        \n   /::::\\   \\:::\\    \\      /::::\\   \\:::\\    \\      /::::\\   \\:::\\    \\      /:::/    \\:::\\    \\        |::|   |        \n  /::::::\\   \\:::\\    \\    /::::::\\   \\:::\\    \\    /::::::\\   \\:::\\    \\    /:::/    / \\:::\\    \\       |::|___|______  \n /:::/\\:::\\   \\:::\\____\\  /:::/\\:::\\   \\:::\\    \\  /:::/\\:::\\   \\:::\\____\\  /:::/    /   \\:::\\    \\      /::::::::\\    \\ \n/:::/  \\:::\\   \\:::|    |/:::/__\\:::\\   \\:::\\____\\/:::/  \\:::\\   \\:::|    |/:::/____/     \\:::\\____\\    /::::::::::\\____\\\n\\::/    \\:::\\  /:::|____|\\:::\\   \\:::\\   \\::/    /\\::/   |::::\\  /:::|____|\\:::\\    \\      \\::/    /   /:::/~~~~/~~      \n \\/_____/\\:::\\/:::/    /  \\:::\\   \\:::\\   \\/____/  \\/____|:::::\\/:::/    /  \\:::\\    \\      \\/____/   /:::/    /         \n          \\::::::/    /    \\:::\\   \\:::\\    \\            |:::::::::/    /    \\:::\\    \\              /:::/    /          \n           \\::::/    /      \\:::\\   \\:::\\____\\           |::|\\::::/    /      \\:::\\    \\            /:::/    /           \n            \\::/____/        \\:::\\   \\::/    /           |::| \\::/____/        \\:::\\    \\           \\::/    /            \n             ~~               \\:::\\   \\/____/            |::|  ~|               \\:::\\    \\           \\/____/             \n                               \\:::\\    \\                |::|   |                \\:::\\    \\                              \n                                \\:::\\____\\               \\::|   |                 \\:::\\____\\                             \n                                 \\::/    /                \\:|   |                  \\::/    /                             \n                                  \\/____/                  \\|___|                   \\/____/                           ")
    print("_"*121)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
def inputExit():
    isIdiot = True
    times = 0
    
    while isIdiot:
        key = input("Press enter to exit...")
        if key != "" and times < 1:
            pass
        elif key != "" and times < 3:
            print("I said enter idiot...")
        elif key != "":
            while True:                
                cls()
                print("Your time, your fun")
                input()                
        else:
            sys.exit()
        times += 1
        time.sleep(1)
        cls()    

data = {}
questionCounter = 0
configPath = "config.json"
hdr = {'User-Agent': 'Mozilla/5.0'}

defaultConfig = {
    "question_path" : "questions.json",
    "sheet_path" : "review",
    "score_path" : "SCORE.txt",    
    "url_path" : "url.txt",
    "multiple_choice" : False,
    "wrong_answer" : 2,
    "number_of_questions" : 32
}

os.system('mode con: cols=135 lines=40')
art()

if os.path.exists(configPath):
    print("Config json found.")
    time.sleep(1)
    with open(configPath) as json_file:
        config = json.load(json_file)
        questionsPath = config["question_path"]
        urlPath = config["url_path"]
else:
    print("Config file doesn't exist!")
    time.sleep(1)
    print("Deployed config.json")
    time.sleep(1)
    with open(configPath, "w") as json_file2:
        json.dump(defaultConfig, json_file2, indent = 4)
        questionsPath = "questions.json"
        urlPath = "url.txt"

if os.path.exists(urlPath):
    print("URL's file found.")
    time.sleep(1)
    print("Retrieving URLs.")
    with open(urlPath,'r') as file2:
        urls = [ url for url in file2] 
else:
    print("URL's file doesn't exist!")
    print("Press enter to exit...")
    input()
    sys.exit()

print("Scraping started.")
file = open("questions.json", "w+")
bar = progressbar.ProgressBar(maxval=len(urls), \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
print("_" * 121)

for i, url in enumerate(urls):
    req = Request(url,headers=hdr)
    page = urlopen(req)
    html = page.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")

    test = soup.find_all('p')
    lines = str(test[1]).split("\n")

    count = 0
    while count < len(lines):
        if re.findall("^<p>[0-9]+", lines[count][:5]):
            
            questionCounter += 1
            question = lines[count].partition(" ")[2][:-5]
            answer = []
            count += 1
            while re.findall("^[a-d]\)", lines[count][:5]):
                answer.append(lines[count][:-5])
                count += 1
            correctAnswer = lines[count][-6]
            explanation = lines[count+1][13:-7]
            
            item = {
                str(questionCounter): {
                        "question" : question,
                        "answer" : answer,
                        "correct" : correctAnswer,
                        "explanation" : explanation
                    }
                }
            data.update(item)
        count += 1
    bar.update(i+1)

cls()
art()
print(questionCounter, "questions were found.") 
json.dump(data, file, indent = 4)
file.close()
print("The questions have been written.")
print("Check config file before taking the quiz!")
inputExit()

    