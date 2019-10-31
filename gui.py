import kluisje as K
from tkinter import *

# kluisje.kluisjecheck(2, 4)
# runt kluisjecheck functie uit file kluisje.py

def toonLoginFrame():
    hoofdframe.pack_forget()
    nieuweKluisFrame.pack_forget()
    tijdFrame.pack_forget()
    kostenFrame.pack_forget()
    loginframe.pack()

def toonHoofdFrame():
    loginframe.pack_forget()
    hoofdframe.pack()

def toonNieuweKluisFrame():
    loginframe.pack_forget()
    nieuweKluisFrame.pack()

def toonTijdFrame():
    loginframe.pack_forget()
    tijdFrame.pack()

def toonKostenFrame():
    loginframe.pack_forget()
    kostenFrame.pack()

def login():
    if loginfield.get() == "admin":
        toonHoofdFrame()
    elif loginfield.get() == "1":
        toonNieuweKluisFrame()
    elif loginfield.get() == "4":
        toonTijdFrame()
    elif loginfield.get() == "2":
        toonKostenFrame()
    else:
        print('Verkeerde gebruikersnaam!')

def kaartNummer():
    nummer = nummerField.get()
    nummer = int(nummer)
    return nummer

#Hiertussen stonden alle functies

root = Tk()
root.configure(height=400, width=600)

loginframe = Frame(master=root)
loginframe.pack(fill="both", expand=True)
loginfield = Entry(master=loginframe)
loginfield.pack(padx=20, pady=20)
loginbutton = Button(master=loginframe, text='Gereed', command=login)
loginbutton.pack(padx=20, pady=20)
tijdButton = Button(master=loginframe, text="Bereken tijd", command=toonTijdFrame())
tijdButton.pack(padx=0, pady=20)
kostenButton = Button(master=loginframe, text="Bereken kosten", command=toonKostenFrame())
kostenButton.pack(padx=0, pady=20)

hoofdframe = Frame(master=root)
hoofdframe.pack(fill="both", expand=True)
backbutton = Button(master=hoofdframe, text='<', command=toonLoginFrame)
backbutton.pack(padx=20, pady=20)

nieuweKluisFrame = Frame(master=root)
nieuweKluisFrame.pack(fill="both", expand=True)
nummerField = Entry(master=nieuweKluisFrame)
tijdButton = Button(master=nieuweKluisFrame, text='Hoe lang is de kluis gereserveerd?', command=toonTijdFrame)
backbutton = Button(master=nieuweKluisFrame, text='<', command=toonLoginFrame)
backbutton.pack(padx=20, pady=20)

tijdFrame = Frame(master=root)
tijdFrame.pack(fill="both", expand=True)
dict = K.huidigeDatum()
tekst = K.totaalMinuten(dict)
label = Label(master=tijdFrame, text= tekst, width= 14, height= 5)
label.pack()
backbutton = Button(master=tijdFrame, text='<', command=toonLoginFrame)
backbutton.pack(padx=20, pady=20)

kostenFrame = Frame(master=root)
kostenFrame.pack(fill="both", expand=True)
kaartnummer = Entry(master=kostenFrame)
nummerButton = Button(master=kostenFrame, text='Volgende', command=kaartNummer)
kosten = K.huidigePrijs(nummerButton)
label = Label(master=kostenFrame, text=kosten)
label.pack()
backbutton = Button(master=kostenFrame, text='<', command=toonLoginFrame)
backbutton.pack(padx=20, pady=20)

toonLoginFrame()
root.mainloop()