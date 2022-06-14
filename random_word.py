import requests
import translators as ts
from translate import Translator
from oxford_dict import*

def translate():
    translator = Translator(from_lang="english", to_lang="polish")

    re = requests.get("https://random-word-api.herokuapp.com/word")
    word = re.text
    word = word.replace("[","").replace("]","")
    print(word)
    oxford = Ox_dict(word)
    merriam = Merriam_webster(word)

    #return oxford.search()
    #name_coll, senses_coll = merriam.search_coll()
    senses_the, name_the = merriam.search_the()
    
    return name_the, senses_the
    #translation = translator.translate(word)
    #print(translation)

    #tr_word = ts.google(word, from_language="en", to_language="pl")
    #print(tr_word)
    
if __name__ == "__main__":
    print(translate())
