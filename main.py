import requests
import json
token = "878137494:AAFq1YmAoh4bMGXeUBPM90hTJUMNdivlqw4"
baseurl = "https://api.telegram.org/bot{}/".format(token)

def getUpdates(offset):
    url = baseurl + "getUpdates?timeout=120"
    if offset:
        url = url + "&offset={}".format(offset + 1)
        print(offset, offset + 1, url)
    result = requests.get(url)
    return json.loads(result.content)

def sendMessage(text, chat_id):
    url = baseurl + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    requests.get(url)

update_id = None
while True:
    bericht = getUpdates(offset=update_id)
    bericht = bericht["result"]
    if bericht:
        for item in bericht:
            update_id = item["update_id"]
            message = item["message"]["text"]
            chat_id = item["message"]["chat"]["id"]
            data = [update_id, message, chat_id]
    if data[1] == '/start':
        sendMessage('stuur "1" voor de huidigekosten die u heeft')