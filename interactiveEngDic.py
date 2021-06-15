'''
    Program: Interactive Python Based English Dic
    Author: Shashi Kumar
    GitHub: sbkshashi
'''
import json
from difflib import get_close_matches

#data = json.load(open("data.json"))
data = json.load(open("interactiveEngDic/data.json"))
#isav = os.path.exists("data.json")
#print(isav)
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data: #If input is ant Noun
        return data[word.title()]
    elif word.upper() in data: #if input is acronames like USA
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if ues, or N if no: " % get_close_matches(word, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The Word does not exist. Please double check it"
        else:
            return "We did not understand your entry"

    else:
        return "The Work does not exist. Please double check it."

word = input("Enter a Word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
