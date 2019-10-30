import requests
import json
token = "878137494:AAFq1YmAoh4bMGXeUBPM90hTJUMNdivlqw4"
baseurl = "https://api.telegram.org/bot{}/".format(token)

def getUpdates(offset):
    url = baseurl + "getUpdates?timeout=120"
    if offset:
        url = url + "&offset={}".format(offset + 1)
    print('started listening')
    result = requests.get(url)
    print('message received', json.loads(result.content))
    return json.loads(result.content)

def sendMessage(text, chat_id):
    url = baseurl + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    requests.get(url)

def ovChipKaartNummerOphalen(chat_id):
    sendMessage('Wat is uw ov-chipkaartnummer?', chat_id)

def commands(update_id, message, chat_id):
    if message == '/huidigeprijs':
        ovChipKaartNummerOphalen(chat_id)
        data = laatsteBerichtOphalen()
        print(data)

def laatsteBerichtOphalen(update_id):
    data = []
    while True:
        bericht = getUpdates(offset=update_id)
        bericht = bericht["result"]
        if bericht:
            print('message not empty')
            for item in bericht:
                update_id = item["update_id"]
                message = item["message"]["text"]
                chat_id = item["message"]["chat"]["id"]
                data = [update_id, message, chat_id]
                print(data)
            return data #gevuld met alles
        return data #lege lijst

x = laatsteBerichtOphalen(None)
commands(x[0], x[1], x[2])