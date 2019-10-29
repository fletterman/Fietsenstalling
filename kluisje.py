#basis
import json, datetime
# from tkinter import *

vandaag = datetime.datetime.today()
beheerder = 111
standaardPrijsUur = 0.30
standaardPrijsMinuut = standaardPrijsUur / 60
# legeKluizen = 0

def kluisCheck(getal):
    legeKluizen = 0
    kaartNummer = int(input("Welke kaartnummer is van u?"))
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

def nieuweKluis():
    teller = 1
    with open("fietsenstallingen.json", 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    kaartNummer = int(input("Welke kaartnummer wordt er gebruikt?"))
    if kluisCheck(1):
        return "\n"
    dictionary = huidigeDatum()
    dictionary['bezet'] = True
    dictionary['kluisNummer'] = len(kluisjes) + 1
    for x in range(len(kluisjes)+1):
        if teller != x['kluisNummer']:
            dictionary['kluisNummer'] = teller
            break
        else:
            teller += 1
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

while True:
    legeKluizen = 0
    optieGui = int(input('111 = Beheerder, 222 = huidigeprijs berekenen, 333 = nieuwe kluis, 444 = kluis inleveren, 555 = resterende tijd berekenen'))
    with open("fietsenstallingen.json", 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    if optieGui == beheerder:
        kluisNummer = int(input("Welke kluisnummer wilt u legen?"))
        kluisNummer -= 1
        kluisjes[kluisNummer]["kaartNummer"] = 0
        kluisjes[kluisNummer]["bezet"] = False
        kluisjes[kluisNummer]["stallingsJaar"], kluisjes[kluisNummer]["stallingsMaand"], kluisjes[kluisNummer]["stallingsDag"], kluisjes[kluisNummer]["stallingsUur"], kluisjes[kluisNummer]["stallingsMinuut"] = 0, 0, 0, 0, 0
        print(kluisjes[kluisNummer])
        continue
    elif optieGui == 222:
        kaartNummer = int(input("wat is uw kaartnummer?"))
        print("Uw prijs is: ", huidigePrijs(kaartNummer))
        continue
    elif optieGui == 333:
        nieuweKluis()
        continue
    elif optieGui == 444:
        pass
    elif optieGui == 555:
        kaartNummer = int(input('Wat is uw kaartnummer?'))
        saldo = int(input('Wat is uw saldo?'))
        resterendSaldo = saldo - huidigePrijs(kaartNummer)
        urenOver = resterendSaldo / standaardPrijsUur
        if urenOver > 0:
            print("U kunt uw fiets nog:", urenOver, "uur stallen")
        else:
            print('U komt:', resterendSaldo, 'tekort.')
        continue
    for x in kluisjes:
        if optieGui == x['kaartNummer']:
            print(kluisjes.index(x) + 1)
            break
        else:
            legeKluizen += 1
            if legeKluizen == len(kluisjes):
                print("U heeft geen kluis in gebruik")
