import requests
import translators as ts
from translate import Translator
from oxford_dict import*

def translate():

    re = requests.get("https://random-word-api.herokuapp.com/word")
    word = re.text
    word = word.replace("[","").replace("]","")
    print(word)
    oxford = Ox_dict(word)
    merriam = Merriam_webster(word)
    merriam.search_coll()
    merriam.search_the()

    return oxford.search()

    #tr_word = ts.google(word, from_language="en", to_language="pl")
    #print(tr_word)
    
if __name__ == "__main__":
    print(translate())
