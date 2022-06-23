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
    oxford = Ox_dict(word)
    merriam = Merriam_webster(word)

    result_coll = merriam.search_coll()
    result_the = merriam.search_the()
    
    return result_coll, result_the, oxford.search()

    #translation = translator.translate(word)
    #print(translation)

    #tr_word = ts.google(word, from_language="en", to_language="pl")
    #print(tr_word)
    
if __name__ == "__main__":
    result_coll, result_the, oxford = translate()
    
    if "empty" in result_coll or "empty" in result_the or "empty" in oxford:
        print(f"Merriam Webster Thesaurus  \n{result_the}\n")
        print(f"Merriam Webster Collegiate \n{result_coll}\n")
        print(f"Oxford Dictionary \n{oxford}")

    else:
        print(f"Merriam Webster Thesaurus  \n{result_the[0]}: {result_the[1]}\n")
        print(f"Merriam Webster Collegiate \n{result_coll[0]}: {result_coll[1]}\n")
        print(f"Oxford Dictionary \n{oxford}")
