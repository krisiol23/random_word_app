import json
import requests

class Ox_dict:
    
    app_id = ""
    app_key = ""

    endpoint = "entries"
    language_code = "en-us"

    def __init__(self, word):
        self.word = word

    def search(self):
        url = "https://od-api.oxforddictionaries.com/api/v2/" + self.endpoint + "/" + self.language_code + "/" + self.word.lower() + "?fields=definitions"

        r = requests.get(url, headers = {"app_id": self.app_id, "app_key": self.app_key})

        #data = json.dumps(r.json())
        g = json.loads(r.text)
        #print(g)
        if "results" in g:
            subsenses = g["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["subsenses"]
            for sub in subsenses:
                return sub["definitions"][0]
        else:
                return "empty" 

class Merriam_webster:
    app_key_coll = ""
    app_key_the = ""
    
    def __init__(self, word):
        self.word = word

    def search_coll(self):
        url = "https://dictionaryapi.com/api/v3/references/collegiate/json/"+ self.word + "?key=" + self.app_key_coll

        r = requests.get(url)
        data = json.loads(r.text)
        print(data)
    def search_the(self):
        url = "https://dictionaryapi.com/api/v3/references/thesaurus/json/"+ self.word + "?key=" + self.app_key_the

        r = requests.get(url)
        data = json.loads(r.text)
        print(data)
        
    
