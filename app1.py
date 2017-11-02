import json
from difflib import get_close_matches

def lookUp(word):
    word.lower()
    if word in data:                                     #query is an exact match to key
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        for i in get_close_matches(word, data.keys()):
            if input("Did you mean %s? Type y or n: " %i).lower() == "y":
                return data[i]
    return -1
#END lookUp

data = json.load(open("data.json"))
word = input("Word: ")
definitions = lookUp(word)

if definitions == -1:
    print("Word does not exist. Please try again.")
else:
    print("We found " + str(len(definitions)) + " definition(s):\n----------------")
    for i in definitions:
        print(i)
