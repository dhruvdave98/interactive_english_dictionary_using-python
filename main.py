# Demonstrates the application, which loads the json file with lots of words,
# and it's meaning in it, user will be asked to enter the word in console, and
# it will get the meaning according to that.
#
# email: dhruvdave61@gmail.com

import json
from difflib import get_close_matches

# loads the json file
data = json.load(open("data.json"))


# processing the word entered by the user can get the meaning of it
def translate(w):
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys(), cutoff=0.8)) > 0:
        answer = input("Did you mean %s instead ? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if answer == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif answer == "N":
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it"


word = input("Enter word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
