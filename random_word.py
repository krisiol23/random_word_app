import requests
import translators as ts
from translate import Translator
import dictionary

def translate():
    translator = Translator(from_lang="english", to_lang="polish")

    re = requests.get("https://random-word-api.herokuapp.com/word")
    word = re.text
    word = word.replace("[","").replace("]","")
    print(word)
    oxford = dictionary.Ox_dict(word)
    merriam = dictionary.Merriam_webster(word)

    name_coll, senses_coll = merriam.search_coll()
    name_the,senses_the= merriam.search_the()
    
    return name_the, senses_the, name_coll, senses_coll, oxford.search()
    #translation = translator.translate(word)
    #print(translation)

    #tr_word = ts.google(word, from_language="en", to_language="pl")
    #print(tr_word)
    
if __name__ == "__main__":
    name_the, senses_the, name_coll, senses_coll, oxford = translate()
    print(f"Merriam Webster Thesaurus  \n{name_the}: {senses_the}\n")
    print(f"Merriam Webster Collegiate \n{name_coll}: {senses_coll}\n")
    print(f"Oxford Dictionary \n{oxford}")
