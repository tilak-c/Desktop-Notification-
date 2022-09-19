from plyer import notification
import time
import  json
import  requests 
import random
import hashlib
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

response = requests.get(word_site)
WORDS = response.content.splitlines()
a=random.randint(0,9999)
word=WORDS[a].decode()
app_id = "f0822e1a"
app_key = "d201184186b092a09d508ee5aa4b8b7c"
endpoint = "entries"
language_code = "en-us"
word_id = word
url = "https://od-api.oxforddictionaries.com/api/v2/" + endpoint + "/" + language_code + "/" + word_id.lower()
r = requests.get(url, headers = {"app_id": app_id, "app_key": app_key})
string=json.dumps(r.json())
json=json.loads(string)
for entry in json['results'][0]['lexicalEntries']:
    pass
if __name__=="__main__":
    while True:
        notification.notify(
            title="Learn a new definition",
            message=entry['text'] + " - " + entry['entries'][0]['senses'][0]['definitions'][0],
            app_icon=r"C:\Users\Tilakavati\Langs\Python\project\learn.ico",
            timeout=12
        )
        time.sleep(60*60)
