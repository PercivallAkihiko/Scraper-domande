import json
import random
import os
import sys
import time
from datetime import datetime

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
        
def shuffleOption(option):
    keys = option.keys()    
    values = option.values()    
    shuffled_values = list(values)    
    random.shuffle(shuffled_values)
    return dict(zip(list(keys), shuffled_values))

questions = []
answered = [-1]
score, correct, blank, wrong = 0, 0, 0, 0

now = datetime.now()
dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
configPath = "config.json"

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
        sheetPath = config["sheet_path"]
        numberQuestion = config["number_of_questions"]
        multipleChoice = config["multiple_choice"]
        scorePath = config["score_path"]
        wrongAnswer = config["wrong_answer"]
else:
    print("Config file doesn't exist!")
    time.sleep(1)
    print("Deployed config.json")
    time.sleep(1)
    with open(configPath, "w") as json_file2:
        json.dump(defaultConfig, json_file2, indent = 4)
        questionsPath = "questions.json"
        sheetPath = "review"
        numberQuestion = 32
        multipleChoice = False
        scorePath = "SCORE.txt"
        wrongAnswer = 2

try:
    os.stat(questionsPath)
except:
    print("Questions not found.")
    time.sleep(1)
    print("Run scraping.py first")
    inputExit()
try:
    os.stat(sheetPath)
except:
    os.mkdir(sheetPath)
    
sheet = open(sheetPath + "/" + dt_string + ".txt", "w+", encoding='utf8')
with open(questionsPath) as json_file:
    data = json.load(json_file)
    questions = [ question for question in data] 

print("Quiz is going to start. Number of question setted on ", str(numberQuestion)+".")
print("Don't type if you want to skip.")
input()

for number in range(1, numberQuestion + 1):
    cls()
    sheet.write("_"*46 + "\n")
    print(number, "of", str(numberQuestion) + "-" )
    print("_"*38)
    
    if len(questions) == 0:
        print("There's no questions left...")
        time.sleep(2)
        break
    
    # randomInt = -1
    # while randomInt in answered:
    #     randomInt = random.choice(questions)
    #     print("SONO QUI")
    #     if len(data[str(randomInt)]["answer"]) < 3 and not multipleChoice:
    #         randomInt = -1
    # answered.append(randomInt)
    
    while True:
        random.shuffle(questions)
        randomInt = questions.pop()
        
        if len(data[str(randomInt)]["answer"]) > 2:
            break
        
    
    print(str(number)+".", data[str(randomInt)]["question"], "\n")
    
    answers = data[str(randomInt)]["answer"]
    correct_answer = data[str(randomInt)]["correct"]
    
    option = {
            "a" : [answers[0][0], answers[0][2:]],
            "b" : [answers[1][0], answers[1][2:]],
            "c" : [answers[2][0], answers[2][2:]],
            "d" : [answers[3][0], answers[3][2:]]
        }
    
    option2 = shuffleOption(option)
    
    print("a)", option2['a'][1])
    print("b)", option2['b'][1])
    print("c)", option2['c'][1])
    print("d)", option2['d'][1])
    
    user_input = input('\nAnswer:')
    user_input = user_input.lower()
    
    if user_input == "" :
        sheet.write("LEFT-BLANK" + "!"*37 + "\n\n")
        blank += 1    
    elif user_input != 'a' and user_input != 'b' and user_input != 'c' and user_input != 'd' :
        sheet.write("WRONG" + "!"*41 + "\n\n")
        score -= wrongAnswer
        wrong += 1
    elif option2[user_input][0] == correct_answer:
        score +=2
        correct += 1
    else:
        sheet.write("WRONG" + "!"*41 + "\n\n")
        score -= wrongAnswer
        wrong += 1
        
    for letter, item in option2.items(): 
        if correct_answer == item[0]:
            correct_answer = letter;            
            break
    
    sheet.write(str(number)+"." + data[str(randomInt)]["question"] + "\n")
    sheet.write("a) " + option2['a'][1] + "\n")
    sheet.write("b) " + option2['b'][1] + "\n")
    sheet.write("c) " + option2['c'][1] + "\n")
    sheet.write("d) " + option2['d'][1] + "\n")
    sheet.write("\nAnswered:" + user_input + "\n")
    sheet.write("Correct answer:" + correct_answer + "\n")
    sheet.write("\nExplanation: " + data[str(randomInt)]["explanation"] + "\n")
    
cls()
print("_"*46 + "\n")
print("Blank::" + str(blank))
print("Wrong:" + str(wrong))
print("Correct:" + str(correct))
print("Final score:" + str(score))
print("_"*46 + "\n")
print("Review your quiz on", sheetPath, "folder." )

sheet.write("_"*46 + "\n")
sheet.write("Blank::" + str(blank) + "\n")
sheet.write("Wrong:" + str(wrong) + "\n")
sheet.write("Correct:" + str(correct) + "\n")
sheet.write("Final score:" + str(score) + "\n")
sheet.write("_"*46 + "\n")
sheet.close()

if len(str(numberQuestion)) == 1:
    numberQuestion = "0" + str(numberQuestion)

file_object = open('SCORES.txt', 'a')
file_object.write(str(numberQuestion) + " "*3 +str(dt_string) + " "*10 + str(score) + "\n")
file_object.close()

inputExit()