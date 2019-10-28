#basis
import json
from tkinter import *

while True:
    kaartNummer = input('Wat is uw kaartnummer?')
    with open("fietsenstallingen.json") as infile:
        kluisjes = infile.read()
    for x in kluisjes:
        if kaartNummer in x:
            print('ja')
        else:
            print('nee')
