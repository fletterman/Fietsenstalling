import requests
import json
import kluisje
token = "878137494:AAFq1YmAoh4bMGXeUBPM90hTJUMNdivlqw4"
baseurl = "https://api.telegram.org/bot{}/".format(token)
ovGegeven, update_id = False, None

def getUpdates(offset=None):
    url = baseurl + "getUpdates?timeout=120"
    if offset:
        url = url + "&offset={}".format(offset + 1)
    result = requests.get(url)
    return json.loads(result.content)

def sendMessage(text, chat_id):
    url = baseurl + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    requests.get(url)

def ovChipKaartOphalen(chat_id, offset):
    sendMessage('Wat is uw ov-chipkaartnummer?', chat_id)
    while True:
        ovchipkaartNummer = getUpdates(offset=offset)
        global update_id
        global ovGegeven
        update_id += 1
        ovGegeven = True
        if ovchipkaartNummer['result']:
            try:
                ovchipkaartNummer = int(ovchipkaartNummer['result'][0]['message']['text'])
            except:
                sendMessage('U moet een getal opleveren bestaande alleen uit cijfers.', chat_id)
                offset += 1
                continue
            return ovchipkaartNummer

while True:
    bericht = getUpdates(offset=update_id)
    # print('hier')
    bericht = bericht["result"]
    if bericht:
        for item in bericht:
            update_id = item["update_id"]
            message = item["message"]["text"]
            chat_id = item["message"]["chat"]["id"]
            if message == '/start':
                ovNummer = ovChipKaartOphalen(chat_id, update_id)
                sendMessage('Dankuwel, U kunt nu uit de volgende commands kiezen:\n1: "/huidigeprijs", hiermee ziet u uw huidige kosten. \n2: "/mijnkluisje", hiermee vindt u uw kluisnummer terug als u die bent vergeten. \n3: "/resterendetijd", hiermee berekent u de resterende tijd dat u uw fiets kan opslaan met uw huidige saldo.', chat_id)
            elif message == '/huidigeprijs':
                pass
            elif message == '/mijnkluisje':
                pass
            elif message == '/resterendetijd':
                pass
            elif ovGegeven == False:
                sendMessage('Met "/start" (zonder aanhalingstekens) kunt u beginnen.', chat_id)
            else:
                sendMessage('U kunt uit de volgende commands kiezen:\n1: "/huidigeprijs", hiermee ziet u uw huidige kosten. \n2: "/mijnkluisje", hiermee vindt u uw kluisnummer terug als u die bent vergeten. \n3: "/resterendetijd", hiermee berekent u de resterende tijd dat u uw fiets kan opslaan met uw huidige saldo.', chat_id)