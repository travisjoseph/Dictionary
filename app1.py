import json
from difflib import get_close_matches

def lookUp(word):
    propperNoun = word.capitalize()
    lowerCase = word.lower()
    #lower case match
    if lowerCase in data:
        return data[lowerCase]
    #propper noun match
    elif propperNoun in data:
        return data[propperNoun]
    #similar lower case
    elif len(get_close_matches(lowerCase, data.keys())) > 0:
        for i in get_close_matches(lowerCase, data.keys()):
            if input("Did you mean %s? Type y or n: " %i).lower() == "y":
                return data[i]
    #similar propper noun
    elif len(get_close_matches(propperNoun, data.keys())) > 0:
        for i in get_close_matches(propperNoun, data.keys()):
            if input("Did you mean %s? Type y or n: " %i).lower() == "y":
                return data[i]
    return -1 #no match found
#END lookUp

data = json.load(open("data.json"))
definitions = lookUp(input("Word: "))

if definitions == -1:
    print("Word does not exist. Please try again.")
else:
    print("We found " + str(len(definitions)) + " definition(s):\n----------------")
    for i in definitions:
        print(i)
