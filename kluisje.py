#basis
import json, datetime
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from tkinter import *
from tkinter.messagebox import showinfo



vandaag = datetime.datetime.today()
beheerder = 111
standaardPrijsUur = 0.30
standaardPrijsMinuut = standaardPrijsUur / 60
# legeKluizen = 0


def kluisCheck(getal, kaartNummer):
    legeKluizen = 0
    if getal == 1:
        for x in kluisjes:
            if kaartNummer == x['kaartNummer']:
                print("U mag maar 1 kluis in gebruik hebben. Leeg uw kluis eerst voordat u een nieuwe aanvraagt")
                return True
    if getal == 2:
        for x in kluisjes:
            if kaartNummer == x['kaartNummer']:
                resultaat = kluisjes.index(x) + 1
                return resultaat
            else:
                legeKluizen += 1
                if legeKluizen == len(kluisjes):
                    resultaat = "U heeft geen kluis in gebruik"
                    return resultaat

def nieuweKluis(kaartNummer):
    teller = 1
    with open("fietsenstallingen.json", 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    if kluisCheck(1, kaartNummer):
        return "\n"
    dictionary = huidigeDatum()
    dictionary['bezet'] = True
    dictionary['kluisNummer'] = len(kluisjes) + 1
    legeLijst = []
    for x in kluisjes:
        legeLijst.append(x['kluisNummer'])
    print(legeLijst)
    for x in kluisjes:
        if teller in legeLijst:
            teller += 1
            continue
        else:
            dictionary['kluisNummer'] = teller
            break
    dictionary['kaartNummer'] = kaartNummer
    kluisjes.append(dictionary)
    resultaat = "U heeft kluisje: {}".format(len(kluisjes))
    with open("fietsenstallingen.json", 'w', encoding='utf-8') as outfile:
        json.dump(kluisjes, outfile, ensure_ascii=False, indent=4)
    return resultaat

def kluisInleveren():
    with open("fietsenstallingen.json", 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    index = kluisCheck(2) - 1
    kluisjes.pop(index)
    with open("fietsenstallingen.json", 'w', encoding='utf-8') as outfile:
        json.dump(kluisjes, outfile, ensure_ascii=False, indent=4)
    tekst = "Uw kluis is ingeleverd"
    return tekst

def huidigePrijs(kaartNummer):
    with open("fietsenstallingen.json", 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    for x in kluisjes:
        if kaartNummer == x["kaartNummer"]:
            prijs = (totaalMinuten(huidigeDatum()) - totaalMinuten(x)) * standaardPrijsMinuut
            return prijs

def totaalMinuten(datumDictionary):
    som = 0
    dagenInMaanden = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for index in range(datumDictionary['stallingsMaand'] + 1):
        som += dagenInMaanden[index]
    antMinuten = ((((som + datumDictionary['stallingsJaar'] * 365 + datumDictionary['stallingsJaar'] // 4) + datumDictionary['stallingsDag']) * 24 + datumDictionary["stallingsUur"]) * 60 + datumDictionary['stallingsMinuut'])  # ant jaar * 365 + 1 dag per vier hele jaren + ant dagen in huidige jaar
    return antMinuten

def huidigeDatum():
    maanden = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    huidigeMaand, huidigeDag, huidigeJaar, huidigeUur, huidigeMinuut = vandaag.strftime('%b'), vandaag.strftime('%d'), vandaag.strftime('%Y'), vandaag.strftime("%H"), vandaag.strftime('%M')
    huidigeMaandNummer = maanden[huidigeMaand]
    datumDictionary = {
        "bezet": False,
        "kaartNummer": 0,
        "kluisNummer": 0,
        "stallingsJaar": int(huidigeJaar),
        "stallingsMaand": int(huidigeMaandNummer),
        "stallingsDag": int(huidigeDag),
        "stallingsUur": int(huidigeUur),
        "stallingsMinuut": int(huidigeMinuut)
    }
    return datumDictionary

########################################################################################################################

def botHuidigePrijs(update, context):
    update.message.reply_text("wat is uw kaartNummer?")
    update.message.reply_text("Uw prijs is: ", huidigePrijs(kaartNummer))
def botKluisjeCheck(kaartNummer, update, context):
    kaartNummer = int(input("wat is uw kaartnummer?"))
def botResterendeTijd(kaartNummer, update, context):
    update.message.reply_text('Hoeveel saldo beschikt u over?')
    x = True
    while x:
        saldo = update.message.text
        try:
            saldo = int(saldo)
            x = False
        except:
            update.message.reply_text('U moet een getal invullen')
    resterendSaldo = saldo - huidigePrijs(kaartNummer)
    urenOver = resterendSaldo / standaardPrijsUur
    if urenOver > 0:
        update.message.reply_text("U kunt uw fiets nog:", urenOver, "uur stallen")
    else:
        update.message.reply_text('U komt:', resterendSaldo, 'tekort.')

def main():
    updater = Updater("878137494:AAFq1YmAoh4bMGXeUBPM90hTJUMNdivlqw4", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("kluisjecheck", botKluisjeCheck()))
    dp.add_handler(CommandHandler("huidigeprijs", botHuidigePrijs()))
    dp.add_handler(CommandHandler("resterendetijd", botResterendeTijd()))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

########################################################################################################################


# while True:
#     legeKluizen = 0
#     optieGui = int(input('111 = Beheerder, 222 = huidigeprijs berekenen, 333 = nieuwe kluis, 444 = kluis inleveren, 555 = resterende tijd berekenen'))
#     with open("fietsenstallingen.json", 'r', encoding='utf-8') as infile:
#         kluisjes = json.load(infile)
#     if optieGui == beheerder:
#         kluisNummer = int(input("Welke kluisnummer wilt u legen?"))
#         kluisNummer -= 1
#         kluisjes[kluisNummer]["kaartNummer"] = 0
#         kluisjes[kluisNummer]["bezet"] = False
#         kluisjes[kluisNummer]["stallingsJaar"], kluisjes[kluisNummer]["stallingsMaand"], kluisjes[kluisNummer]["stallingsDag"], kluisjes[kluisNummer]["stallingsUur"], kluisjes[kluisNummer]["stallingsMinuut"] = 0, 0, 0, 0, 0
#         print(kluisjes[kluisNummer])
#         continue
#     elif optieGui == 222:
#         kaartNummer = int(input("wat is uw kaartnummer?"))
#         print("Uw prijs is: ", huidigePrijs(kaartNummer))
#         continue
#     elif optieGui == 333:
#         kaartNummer = int(input("wat is uw kaartnummer?"))
#         nieuweKluis(kaartNummer)
#         continue
#     elif optieGui == 444:
#         kluisInleveren()
#         continue
#     elif optieGui == 555:
#         kaartNummer = int(input('Wat is uw kaartnummer?'))
#         saldo = int(input('Wat is uw saldo?'))
#         resterendSaldo = saldo - huidigePrijs(kaartNummer)
#         urenOver = resterendSaldo / standaardPrijsUur
#         if urenOver > 0:
#             print("U kunt uw fiets nog:", urenOver, "uur stallen")
#         else:
#             print('U komt:', resterendSaldo, 'tekort.')
#         continue
#     for x in kluisjes:
#         if optieGui == x['kaartNummer']:
#             print(kluisjes.index(x) + 1)
#             break
#         else:
#             legeKluizen += 1
#             if legeKluizen == len(kluisjes):
#                 print("U heeft geen kluis in gebruik")
#     elif kaartNummer == "q":
#         False

# def clicked():
#     bericht = 'Dit een bericht voor de gebruiker!'
#     showinfo(title='popup', message=bericht)
#
# root = Tk()
# button = Button(master=root, text='Druk hier', command=clicked)
# button.pack(pady=10)
#
# root.mainloop()