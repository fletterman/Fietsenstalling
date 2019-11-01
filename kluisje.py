import json, datetime
# from tkinter import *

# def clicked():
#     bericht = 'Dit een bericht voor de gebruiker!'
#     showinfo(title='popup', message=bericht)

vandaag = datetime.datetime.today()
beheerder = 111
standaardPrijsUur = 0.30
standaardPrijsMinuut = standaardPrijsUur / 60

def kluisCheck(optie, kaartNummer):
    legeKluizen = 1
    with open("fietsenstallingen.json", 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    if optie == 1:
        for x in kluisjes:
            if kaartNummer == x['kaartNummer']:
                resultaat = ["U mag maar 1 kluis in gebruik hebben. Leeg uw kluis eerst voordat u een nieuwe aanvraagt", True]
                return resultaat
        resultaat = ["", False]
        return resultaat
    if optie == 2:
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
    test = kluisCheck(1,kaartNummer)
    if test[1]:
        return test[0]
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
    resultaat = "U heeft kluisje: {}".format(dictionary['kluisNummer'])
    with open("fietsenstallingen.json", 'w', encoding='utf-8') as outfile:
        json.dump(kluisjes, outfile, ensure_ascii=False, indent=4)
    return resultaat

def kluisInleveren(kaartnummer):
    with open("fietsenstallingen.json", 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    index = kluisCheck(2, kaartnummer)
    if isinstance(index, str):
        return index
    else:
        index -= 1
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
    geenKluis = "U heeft geen kluis in gebruik en heeft dus ook geen kosten"
    return geenKluis

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

def stalTijd(kaartnummer):
    datumDictionary = huidigeDatum()
    huidigeTijd = totaalMinuten(datumDictionary)
    locatie = 0
    teller = 0
    with open('fietsenstallingen.json', 'r', encoding='utf-8') as infile:
        kluisjes = json.load(infile)
    for x in kluisjes:
        if kaartnummer == x['kaartNummer']:
            locatie = kluisjes.index(x)
        else:
            teller += 1
    stallingsTijd = totaalMinuten(kluisjes[locatie])
    duur = huidigeTijd - stallingsTijd
    return duur

# root = Tk()
# button = Button(master=root, text='Druk hier', command=clicked)
# button.pack(pady=10)
#
# root.mainloop()


'''hieronder is de console test code, deze is nu obsolete'''

# while True:
#     legeKluizen = 0
#     optieGui = ""
#     optieGuiString = input('111 = Beheerder, 222 = huidigeprijs berekenen, 333 = nieuwe kluis, 444 = kluis inleveren, 555 = resterende tijd berekenen')
#     if optieGuiString == 'q':
#         break
#     else:
#         optieGui = int(optieGuiString)
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
#     elif optieGui == "q":
#         False
#     for x in kluisjes:
#         if optieGui == x['kaartNummer']:
#             print(kluisjes.index(x) + 1)
#             break
#         else:
#             legeKluizen += 1
#             if legeKluizen == len(kluisjes):
#                 print("U heeft geen kluis in gebruik")
#
#
#
