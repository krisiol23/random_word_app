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

        data = json.loads(r.text)
        
        if "results" in data:
            subsenses = data["results"][0]["lexicalEntries"][0]["entries"][0]["senses"][0]["subsenses"]
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
        try:
            senses = data[0].get("shortdef")
            name = data[0].get("meta").get("id")
            
            if not senses:
                return "empty" 
            else:
                return [name, senses]
        except:
            return "empty"
        
    def search_the(self):
        url = "https://dictionaryapi.com/api/v3/references/thesaurus/json/"+ self.word + "?key=" + self.app_key_the

        r = requests.get(url)
        data = json.loads(r.text)
        try:
            senses = data[0].get("shortdef")
            name = data[0].get("meta").get("id")
            
            if not senses:
                return "empty"
            else:
                return [name,senses]
        except:
            return "empty"
           
