import random
from tkinter import *
import main as K

# kluisje.kluisjecheck(2, 4)
# runt kluisjecheck functie uit file main.py

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

def nummerGenerator():
    nummer = random.randrange(0,25)
    return nummer

def kostenBerekenen():
    nummer = nummerGenerator()
    nummer = int(nummer)
    kosten = K.huidigePrijs(nummer)
    kostenLabel["text"] = kosten

def nieuweKluis():
    nummer = nummerGenerator()
    nummer = int(nummer)
    resultaat = K.nieuweKluis(nummer)
    nieuweKluis["text"] = resultaat

def inleverenKluis():
    nummer = nummerGenerator()
    nummer = int(nummer)
    inleveren = K.kluisInleveren(nummer)
    inleverenLabel["text"] = inleveren

def tijdBerekenen():
    nummer = nummerGenerator()
    nummer = int(nummer)
    tijd = K.stalTijd(nummer)
    tijdBericht = "U heeft uw kluis al {} minuten in gebruik\n".format(tijd)
    if isinstance(tijd, str):
        tijdBericht = "U heeft geen kluis in gebruik"
        tijdLabel["text"] = tijdBericht
    bericht = tijdBericht + "Uw kaartnummer is: " + str(nummer)
    tijdLabel["text"] = bericht

#Hiertussen stonden alle functies

root = Tk()

loginframe = Frame(master=root, background='yellow')
loginframe.pack(fill="both", expand=True)
welkom = "Welkom bij de ov-staller"
welkomLabel = Label(master=loginframe, text=welkom, background='yellow')
welkomLabel.pack(pady=10)
nieuweKluisButton = Button(master=loginframe, text='Nieuwe kluis', command=toonNieuweKluisFrame)
nieuweKluisButton.pack(side=LEFT, padx=10, pady=20)
inleverenKluisButton = Button(master=loginframe, text='Kluis inleveren', command=toonInleverenKluisFrame)
inleverenKluisButton.pack(side=LEFT, padx=10, pady=20)
tijdButton = Button(master=loginframe, text="Bereken tijd", command=toonTijdFrame)
tijdButton.pack(side=LEFT, padx=10, pady=20)
kostenButton = Button(master=loginframe, text="Bereken kosten", command=toonKostenFrame)
kostenButton.pack(side=LEFT, padx=10, pady=20)
label = Label(master=loginframe, width=10, height=20, background='yellow')
label.pack()

hoofdframe = Frame(master=root, background='yellow')
hoofdframe.pack(fill="both", expand=True)
backbutton = Button(master=hoofdframe, text='<', command=toonLoginFrame)
backbutton.pack(padx=50, pady=20)

nieuweKluisFrame = Frame(master=root, background='yellow')
nieuweKluisFrame.pack(fill="both", expand=True)
nummerField = Entry(master=nieuweKluisFrame)
nummerField.pack(pady=20)
kaartNummer = Button(master=nieuweKluisFrame, text='Volgende', command=nieuweKluis)
kaartNummer.pack(pady=10)
backbutton = Button(master=nieuweKluisFrame, text='<', command=toonLoginFrame)
backbutton.pack(padx=20, pady=20)
nieuweKluis = Label(master=nieuweKluisFrame, text="", width=80, height=20, background='yellow')
nieuweKluis.pack()

inleverenKluisFrame = Frame(master=root, background='yellow')
inleverenKluisFrame.pack(fill="both", expand=True)
vraag = "Welke kaartnummer is van u?"
vraagLabel = Label(master=inleverenKluisFrame, text=vraag, background='yellow')
vraagLabel.pack()
inleverenKluisEntry = Entry(master=inleverenKluisFrame)
inleverenKluisEntry.pack(pady=5)
inleverenKluisButton = Button(master=inleverenKluisFrame, text='Volgende', command=inleverenKluis)
inleverenKluisButton.pack(pady=10)
backbutton = Button(master=inleverenKluisFrame, text='<', command=toonLoginFrame)
backbutton.pack(padx=20, pady=20)
inleverenLabel = Label(master=inleverenKluisFrame, width=80, height=20, background='yellow')
inleverenLabel.pack(pady=10)

tijdFrame = Frame(master=root, background='yellow')
tijdFrame.pack(fill="both", expand=True)
vraag = "Wat is uw kaartnummer?"
label = Label(master=tijdFrame, text=vraag, background='yellow')
label.pack(pady=10)
tijdAanvraag = Entry(master=tijdFrame)
tijdAanvraag.pack(pady=5)
tijdAanvraagButton = Button(master=tijdFrame, text='Volgende', command=tijdBerekenen)
tijdAanvraagButton.pack(pady=5)
backbutton = Button(master=tijdFrame, text='<', command=toonLoginFrame)
backbutton.pack(padx=20, pady=20)
tijdLabel = Label(master=tijdFrame, text="", width=80, height=20, background='yellow')
tijdLabel.pack()

kostenFrame = Frame(master=root, background='yellow')
kosten = "Was is uw kaartnummer?"
kostenVraag = Label(master=kostenFrame, text=kosten, background='yellow')
kostenVraag.pack(pady=10)
kostenFrame.pack(fill="both", expand=True)
kaartnummer = Entry(master=kostenFrame)
kaartnummer.pack(pady=10)
nummerButton = Button(master=kostenFrame, text='Volgende', command=kostenBerekenen, background='blue')
nummerButton.pack(pady=20)
backbutton = Button(master=kostenFrame, text='<', command=toonLoginFrame)
backbutton.pack(pady=20)
kostenLabel = Label(master=kostenFrame, text="", width=80, height=20, background='yellow')
kostenLabel.pack()

toonLoginFrame()
root.mainloop()
