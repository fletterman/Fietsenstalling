import kluisje as K
from tkinter import *

# kluisje.kluisjecheck(2, 4)
# runt kluisjecheck functie uit file kluisje.py

def toonLoginFrame():
    hoofdframe.pack_forget()
    nieuweKluisFrame.pack_forget()
    tijdFrame.pack_forget()
    kostenFrame.pack_forget()
    inleverenKluisFrame.pack_forget()
    loginframe.pack()

def toonHoofdFrame():
    loginframe.pack_forget()
    hoofdframe.pack()

def toonNieuweKluisFrame():
    loginframe.pack_forget()
    nieuweKluisFrame.pack()

def toonInleverenKluisFrame():
    loginframe.pack_forget()
    inleverenKluisFrame.pack()

def toonTijdFrame():
    loginframe.pack_forget()
    tijdFrame.pack()

def toonKostenFrame():
    loginframe.pack_forget()
    kostenFrame.pack()

# def login():
#     if loginfield.get() == "admin":
#         toonHoofdFrame()
#     elif loginfield.get() == "1":
#         toonNieuweKluisFrame()
#     elif loginfield.get() == "4":
#         toonTijdFrame()
#     elif loginfield.get() == "2":
#         toonKostenFrame()
#     else:
#         print('Verkeerde gebruikersnaam!')

def kostenBerekenen():
    nummer = kaartnummer.get()
    nummer = int(nummer)
    kosten = K.huidigePrijs(nummer)
    label = Label(master=kostenFrame, text=kosten, width=50, height=20)
    label.pack()

def nieuweKluis():
    nummer = nummerField.get()
    nummer = int(nummer)
    resultaat = K.nieuweKluis(nummer)
    label = Label(master=nieuweKluisFrame, text=resultaat)
    label.pack()

def inleverenKluis():
    nummer = inleverenKluisEntry.get()
    nummer = int(nummer)
    inleveren = K.kluisInleveren(nummer)
    label = Label(master=inleverenKluisFrame, text=inleveren)
    label.pack()

def tijdBerekenen():
    nummer = tijdAanvraag.get()
    nummer = int(nummer)
    tijd = K.stalTijd(nummer)
    label = Label(master=tijdFrame, text=tijd)
    label.pack()

#Hiertussen stonden alle functies

root = Tk()

loginframe = Frame(master=root)
loginframe.pack(fill="both", expand=True)

nieuweKluisButton = Button(master=loginframe, text='Nieuwe kluis', command=toonNieuweKluisFrame)
nieuweKluisButton.pack(side=LEFT, padx=50, pady=20)
inleverenKluisButton = Button(master=loginframe, text='Kluis inleveren', command=toonInleverenKluisFrame)
inleverenKluisButton.pack(side=LEFT, padx=50, pady=20)
tijdButton = Button(master=loginframe, text="Bereken tijd", command=toonTijdFrame)
tijdButton.pack(side=LEFT, padx=50, pady=20)
kostenButton = Button(master=loginframe, text="Bereken kosten", command=toonKostenFrame)
kostenButton.pack(side=LEFT, padx=50, pady=20)
label = Label(master=loginframe, width=20, height=20)
label.pack()

hoofdframe = Frame(master=root)
hoofdframe.pack(fill="both", expand=True)
backbutton = Button(master=hoofdframe, text='<', command=toonLoginFrame)
backbutton.pack(padx=50, pady=20)

nieuweKluisFrame = Frame(master=root)
nieuweKluisFrame.pack(fill="both", expand=True)
nummerField = Entry(master=nieuweKluisFrame)
nummerField.pack(pady=20)
kaartNummer = Button(master=nieuweKluisFrame, text='Volgende', command=nieuweKluis)
kaartNummer.pack(pady=10)
backbutton = Button(master=nieuweKluisFrame, text='<', command=toonLoginFrame)
backbutton.pack(padx=20, pady=20)
label = Label(master=nieuweKluisFrame, width=50, height=5)
label.pack()

inleverenKluisFrame = Frame(master=root)
inleverenKluisFrame.pack(fill="both", expand=True)
vraag = "Welke kaartnummer is van u?"
label = Label(master=inleverenKluisFrame, text=vraag)
label.pack(pady=10)
inleverenKluisEntry = Entry(master=inleverenKluisFrame)
inleverenKluisEntry.pack(pady=5)
inleverenKluisButton = Button(master=inleverenKluisFrame, text='Volgende', command=inleverenKluis)
inleverenKluisButton.pack()
backbutton = Button(master=inleverenKluisFrame, text='<', command=toonLoginFrame)
backbutton.pack(padx=20, pady=20)

tijdFrame = Frame(master=root)
tijdFrame.pack(fill="both", expand=True)
vraag = "Wat is uw kaartnummer?"
label = Label(master=tijdFrame, text=vraag)
label.pack(pady=10)
tijdAanvraag = Entry(master=tijdFrame)
tijdAanvraag.pack(pady=5)
tijdAanvraagButton = Button(master=tijdFrame, text='Volgende', command=tijdBerekenen)
tijdAanvraagButton.pack(pady=5)
backbutton = Button(master=tijdFrame, text='<', command=toonLoginFrame)
backbutton.pack(padx=20, pady=20)

kostenFrame = Frame(master=root)
kostenFrame.pack(fill="both", expand=True)
kaartnummer = Entry(master=kostenFrame)
kaartnummer.pack(pady=10)
nummerButton = Button(master=kostenFrame, text='Volgende', command=kostenBerekenen)
nummerButton.pack(pady=20)
backbutton = Button(master=kostenFrame, text='<', command=toonLoginFrame)
backbutton.pack(pady=20)
label = Label(master=kostenFrame, width=50, height=5)
label.pack()

toonLoginFrame()
root.mainloop()
