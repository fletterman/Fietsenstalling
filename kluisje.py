#basis
import json, datetime
# from tkinter import *

vandaag = datetime.datetime.today()
beheerder = 111

def nieuweKluis(kaartNummer):
    with open("fietsenstallingen.json", 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    print(kluisjes)
    bezet = True
    dictionary = houdigeDatum()
    dictionary['bezet'] = bezet
    dictionary['kaartNummer'] = kaartNummer
    print(dictionary)
    kluisjes.append(dictionary)
    with open("fietsenstallingen.json", 'w', encoding='utf-8') as outfile:
        json.dump(kluisjes, outfile, ensure_ascii=False, indent=4)

def totaalMinuten(datumDictionary):
    som = 0
    dagenInMaanden = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for index in range(datumDictionary['stallingsMaand'] + 1):
        som += dagenInMaanden[index]
    antMinuten = (((som + datumDictionary['stallingsJaar'] * 365 + datumDictionary['stallingsJaar'] // 4) * 24 + datumDictionary['stallingsDag']) * 60 + datumDictionary['stallingsMinuut'])  # ant jaar * 365 + 1 dag per vier hele jaren + ant dagen in huidige jaar
    return antMinuten
def huidigeDatum():
    maanden = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    huidigeMaand, huidigeDag, huidigeJaar, huidigeUur, huidigeMinuut = vandaag.strftime('%b'), vandaag.strftime('%d'), vandaag.strftime('%Y'), vandaag.strftime("%H"), vandaag.strftime('%M')
    huidigeMaandNummer = maanden[huidigeMaand]
    datumDictionary = {
        "bezet": False,
        "kaartNummer": 0,
        "stallingsJaar": int(huidigeJaar),
        "stallingsMaand": int(huidigeMaandNummer),
        "stallingsDag": int(huidigeDag),
        "stallingsUur": int(huidigeUur),
        "stallingsMinuut": int(huidigeMinuut)
    }
    return datumDictionary

while True:
    legeKluizen = 0
    kaartNummer = int(input('Wat is uw kaartnummer?'))
    with open("fietsenstallingen.json", 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    if kaartNummer == beheerder:
        kluisNummer = int(input("Welke kluisnummer wilt u legen?"))
        kluisNummer -= 1
        kluisjes[kluisNummer]["kaartNummer"] = 0
        kluisjes[kluisNummer]["bezet"] = False
        kluisjes[kluisNummer]["stallingsJaar"], kluisjes[kluisNummer]["stallingsMaand"], kluisjes[kluisNummer]["stallingsDag"], kluisjes[kluisNummer]["stallingsUur"], kluisjes[kluisNummer]["stallingsMinuut"] = 0, 0, 0, 0, 0
        print(kluisjes[kluisNummer])
        continue
    elif kaartNummer == 222:

        continue
    elif kaartNummer == 333:
        nieuweKluis()
        continue
    for x in kluisjes:
        if kaartNummer == x['kaartNummer']:
            print(kluisjes.index(x) + 1)
            break
        else:
            legeKluizen += 1
            if legeKluizen == len(kluisjes):
                print("U heeft geen kluis in gebruik")