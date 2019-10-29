#basis
from tkinter import *
def stallingsTijd(stallingsDatum):
    som = 0
    vandaag = datetime.datetime.today()
    dagenInMaanden = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    maanden = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    huidigeMaand, huidigeDag, huidigeJaar, huidigeUur, huidigeMinuut = vandaag.strftime('%b'), vandaag.strftime('%d'), vandaag.strftime('%Y'), vandaag.strftime("%H"), vandaag.strftime('%M')
    huidigeMaandNummer = maanden[huidigeMaand]
    for x  in range(huidigeMaandNummer + 1): #ant dagen in huidige jaar berekenen door
        som += dagenInMaanden[x]
    #antHuidigeMinuten is optelling van aantal dagen in huidige aantal verstreken maanden + aantal jaar * 365 + 1 per vier gehele jaren + aantal huidige dagen.
    #Dat keer 24 om naar uren te gaan, dat plus antHuidigeUren. Dat keer 60 plus huidigeMinuten voor het aantal huidige minuten die verstreken zijn sinds 0/0/0/0/0
    antHuidigeMinuten = (((som + int(huidigeJaar) * 365 + int(huidigeJaar) // 4) * 24 + int(huidigeDag)) * 60 + int(huidigeMinuut)) #ant jaar * 365 + 1 dag per vier hele jaren + ant dagen in huidige jaar
    print(antHuidigeMinuten)
    print(huidigeJaar, huidigeMaandNummer, huidigeDag, huidigeUur, huidigeMinuut)
beheerder = 111
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
        stallingsTijd('waardelozeWaarde')
        continue
    for x in kluisjes:
        if kaartNummer == x['kaartNummer']:
            print(kluisjes.index(x) + 1)
            break
        else:
            legeKluizen += 1
            if legeKluizen == len(kluisjes):
                print("U heeft geen kluis in gebruik")