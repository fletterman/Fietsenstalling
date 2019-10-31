import requests, json, kluisje
#kluisje import verbeteren door middel van classes in kluisje, alle onnodige junk ook uit kluisje halen.
token = "878137494:AAFq1YmAoh4bMGXeUBPM90hTJUMNdivlqw4"
baseurl = "https://api.telegram.org/bot{}/".format(token)
ovGegeven, update_id, ovNummer = False, None, None
#de bot is te bereiken met @FietsenZuilBot via telegram
#zoek "@FietsenZuilBot" op in de search bar.
#run bot.py op pycharm of op jouw gekozen manier met kluisje.py en fietsenstallingen.json in dezelfde folder.
#stuur /start naar de bot. De rest spreek voor zichzelf.

def getUpdates(offset=None):
    url = baseurl + "getUpdates?timeout=120"
    if offset:
        url = url + "&offset={}".format(offset + 1)
    result = requests.get(url)
    return json.loads(result.content)

def sendMessage(text, chat_id):
    url = baseurl + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    requests.get(url)

def volgendeBerichtOphalen(chat_id, offset, vraag, isINT, isOV):
    sendMessage(vraag, chat_id)
    while True:
        bericht = getUpdates(offset=offset)
        global update_id
        update_id += 1
        if isINT:
            if bericht['result']:
                try:
                    Nummer = int(bericht['result'][0]['message']['text'])
                except:
                    sendMessage('U moet een getal opleveren bestaande alleen uit cijfers.', chat_id)
                    offset += 1
                    continue
                if isOV:
                    
                    global ovGegeven
                    ovGegeven = True
                return Nummer
        else:
            if bericht['result']:
                return bericht['result'][0]['message']['text']

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
                ovNummer = volgendeBerichtOphalen(chat_id, update_id, 'Wat is uw ov-chipkaartnummer?', True, True)
                sendMessage('Dankuwel, U kunt nu uit de volgende commands kiezen:\n1: "/huidigeprijs", hiermee ziet u uw huidige kosten. \n2: "/mijnkluisje", hiermee vindt u uw kluisnummer terug als u die bent vergeten. \n3: "/resterendetijd", hiermee berekent u de resterende tijd dat u uw fiets kan opslaan met uw huidige saldo.', chat_id)
            elif message == '/huidigeprijs':
                if ovGegeven == False:
                    ovNummer = volgendeBerichtOphalen(chat_id, update_id, 'Wat is uw ov-chipkaartnummer?', True, True)
                huidigePrijs = kluisje.huidigePrijs(ovNummer)
                sendMessage("Uw huidige prijs is: "+ str(huidigePrijs) + " euro.", chat_id)
            elif message == '/mijnkluisje':
                if ovGegeven == False:
                    ovNummer = volgendeBerichtOphalen(chat_id, update_id, 'Wat is uw ov-chipkaartnummer?', True, True)
                yz = kluisje.kluisCheck(2, ovNummer)
                sendMessage('U heeft kluisje: ' + str(yz) + ' in gebruik.', chat_id)
            elif message == '/resterendetijd':
                if ovGegeven == False:
                    ovNummer = volgendeBerichtOphalen(chat_id, update_id, 'Wat is uw ov-chipkaartnummer?', True, True)
                saldo = volgendeBerichtOphalen(chat_id, update_id, 'Wat is uw ov-chipkaart saldo?', True, False)
                resterendeSaldo = saldo - kluisje.huidigePrijs(ovNummer)
                urenOver = resterendeSaldo / kluisje.standaardPrijsUur
                if urenOver > 0:
                    sendMessage("U kunt uw fiets nog: " + str(urenOver) + " uur stallen met uw huidige saldo.", chat_id)
                else:
                    sendMessage("U komt: " + str(abs(resterendeSaldo)) + " euro tekort.", chat_id)
            elif ovGegeven == False:
                sendMessage('Met "/start" (zonder aanhalingstekens) kunt u beginnen.', chat_id)
            else:
                sendMessage('U kunt uit de volgende commands kiezen:\n1: "/huidigeprijs", hiermee ziet u uw huidige kosten. \n2: "/mijnkluisje", hiermee vindt u uw kluisnummer terug als u die bent vergeten. \n3: "/resterendetijd", hiermee berekent u de resterende tijd dat u uw fiets kan opslaan met uw huidige saldo.', chat_id)