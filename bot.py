import requests, json, main
#kluisje import verbeteren door middel van classes in kluisje, alle onnodige junk ook uit kluisje halen.
token = "878137494:AAFq1YmAoh4bMGXeUBPM90hTJUMNdivlqw4"
baseurl = "https://api.telegram.org/bot{}/".format(token)
ovGegeven, update_id, ovNummer = False, None, None
#de bot is te bereiken met @FietsenZuilBot via telegram
#zoek "@FietsenZuilBot" op in de search bar.
#run bot.py op pycharm of op jouw gekozen manier met main.py en fietsensstallingen.json in dezelfde folder.
#stuur /start naar de bot. De rest spreek voor zichzelf.

def getUpdates(offset=None):
    """Haalt het volgende bericht op van de gebruiker en returnd dat"""
    url = baseurl + "getUpdates?timeout=120"
    if offset:
        url = url + "&offset={}".format(offset + 1)
    result = requests.get(url)
    return json.loads(result.content)

def sendMessage(text, chat_id):
    """Stuurt een bericht naar het gegeven chat_id."""
    url = baseurl + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    requests.get(url)

def volgendeBerichtOphalen(chat_id, offset, vraag, isINT, isOV):
    """"Stuurt een bericht naar de gebruiker waarin gevraagd wordt naar het gewenste gegeven.
    Als een bericht een integer moet zijn dan probeert de functie de string om te zetten naar een int,
    lukt dit niet dan wordt een foutmelding gestuurd naar de gebruiker en wordt er opnieuw gewacht naar het volgende bericht.
    Als het bericht een ov kaartnummer moet zijn dan gaat het na of de gegeven kaartnummer in de JSON file staat.
    Als het volgens de opties niet goed is opgegeven word het opnieuw gevraagd totdat het goed is.
    De return is een int of string (afhankelijk van de gekozen optie) gemaakt uit het laatst gestuurde bericht van de gebruiker.
    """
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
                    if main.kluisCheck(Nummer)[1]:
                        global ovGegeven
                        ovGegeven = True
                        return Nummer
                    else:
                        sendMessage('Uw OV is nog niet in gebruik, probeer het met een ander OV die wel in gebruik is.', chat_id)
                        offset += 1
                        continue
                return Nummer
        else:
            if bericht['result']:
                return bericht['result'][0]['message']['text']

while True:
    #haal het laatste bericht op.
    bericht = getUpdates(offset=update_id)
    bericht = bericht["result"]
    if bericht:
        for item in bericht:
            #ga door tot het aller laatste bericht en maak variables aan voor de belangrijke items.
            update_id = item["update_id"]
            message = item["message"]["text"]
            chat_id = item["message"]["chat"]["id"]
        #lees het bericht en voer de juiste 'command' uit.
        if message == '/start':
            #hiermee start de code, de ov kaartnummer word gelijk opgevraagd en daarna worden alle andere commands in een textbericht gestuurd.
            ovNummer = volgendeBerichtOphalen(chat_id, update_id, 'Wat is uw ov-chipkaartnummer?', True, True)
            sendMessage('Dankuwel, U kunt nu uit de volgende commands kiezen:\n1: "/huidigeprijs", hiermee ziet u uw huidige kosten. \n2: "/mijnkluisje", hiermee vindt u uw kluisnummer terug als u die bent vergeten. \n3: "/resterendetijd", hiermee berekent u de resterende tijd dat u uw fiets kan opslaan met uw huidige saldo. \n4: "/huidigetijd", hiermee ziet u hoelang uw fiets al gestald staat.', chat_id)
        elif message == '/huidigeprijs':
            #huidigerpijs sturen van gegeven kaartnummer
            if ovGegeven == False:
                ovNummer = volgendeBerichtOphalen(chat_id, update_id, 'Wat is uw ov-chipkaartnummer?', True, True)
            huidigePrijs = main.huidigePrijs(ovNummer)
            sendMessage("Uw huidige prijs is: {:.2f} euro.".format(huidigePrijs), chat_id)
        elif message == '/mijnkluisje':
            #kluisjenummer terug sturen wat gekoppelt is aan het kaartnummer.
            if ovGegeven == False:
                ovNummer = volgendeBerichtOphalen(chat_id, update_id, 'Wat is uw ov-chipkaartnummer?', True, True)
            sendMessage('U heeft kluisje {} in gebruik.'.format(main.kluisIndex(ovNummer)), chat_id)
        elif message == '/resterendetijd':
            #resterende tijd berekenen met een gegeven saldo.
            if ovGegeven == False:
                ovNummer = volgendeBerichtOphalen(chat_id, update_id, 'Wat is uw ov-chipkaartnummer?', True, True)
            saldo = volgendeBerichtOphalen(chat_id, update_id, 'Wat is uw ov-chipkaart saldo?', True, False)
            resterendeSaldo = saldo - main.huidigePrijs(ovNummer)
            urenOver = resterendeSaldo / main.standaardPrijsUur
            #in een goed format de tijd naar de gebruiker sturen
            if urenOver > 24:
                dagenOver = urenOver // 24
                urenOver = urenOver % 24
                sendMessage("U kunt uw fiets nog: {} dagen en {:.1f} uur stallen met uw huidige saldo.".format(int(dagenOver), urenOver), chat_id)
            elif urenOver > 0:
                sendMessage("U kunt uw fiets nog: {:.2f} uur stallen met uw huidige saldo.".format(urenOver), chat_id)
            else:
                sendMessage("U komt: {:.2f} euro tekort.".format(abs(resterendeSaldo)), chat_id)
        elif message == '/huidigetijd':
            #berekenen hoe lang de fiets al gestalt staat.
            if ovGegeven == False:
                ovNummer = volgendeBerichtOphalen(chat_id, update_id, 'Wat is uw ov-chipkaartnummer?', True, True)
            minuten = main.stalTijd(ovNummer)
            minutenrest = minuten % 60
            uren = minuten // 60
            urenrest = uren % 24
            dagen = uren // 24
            if dagen > 0:
                sendMessage('uw fiets staat al {} dagen en {} uur gestalt.'.format(dagen, urenrest), chat_id)
            elif uren > 0:
                sendMessage('Uw fiets staat al {} uur en {} minuten gestalt'.format(uren, minutenrest), chat_id)
            elif minuten < 60:
                sendMessage('Uw fiets staat al {} minuten gestalt.'.format(minuten), chat_id)
        elif ovGegeven == False:
            #als er iets wordt gestuurd wat geen command is terwijl er nog geen OV is gegeven wordt het volgende bericht naar de gebruiker verstuurd
            sendMessage('Met "/start" (zonder aanhalingstekens) kunt u beginnen.', chat_id)
        else:
            #als er iets wordt gestuurd wat geen command is terwijl er al wel een ov is gegeven wordt het volgende bericht naar de gebruiker verstuurd
            sendMessage('U kunt uit de volgende commands kiezen:\n1: "/huidigeprijs", hiermee ziet u uw huidige kosten. \n2: "/mijnkluisje", hiermee vindt u uw kluisnummer terug als u die bent vergeten. \n3: "/resterendetijd", hiermee berekent u de resterende tijd dat u uw fiets kan opslaan met uw huidige saldo. \n4: "/huidigetijd", hiermee ziet u hoe lang uw fiets al gestalt staat.', chat_id)