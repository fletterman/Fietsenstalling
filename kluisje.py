#basis
import json
import datetime
from tkinter import *
def stallingsTijd(stallingsDatum):
    vandaag = datetime.datetime.today()
    Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec = 31, 28, 31, 30, 31, 30, 31, 31,30, 31, 30, 31
    maanden = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
    huidigeMaand, huidigeDag, huidigeJaar, huidigeUur, huidigeMinuut = vandaag.strftime('%b'), vandaag.strftime('%d'), vandaag.strftime('%Y'), vandaag.strftime("%H"), vandaag.strftime('%M')
    huidigeMaandNummer = maanden[huidigeMaand]
    print(huidigeJaar, huidigeMaandNummer, huidigeDag, huidigeUur, huidigeMinuut)
beheerder = 111
while True:
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
    for x in kluisjes:
        if kaartNummer == x['kaartNummer']:
            print(kluisjes.index(x) + 1)
            break
        else:
            print("U heeft geen kluis in gebruik")
