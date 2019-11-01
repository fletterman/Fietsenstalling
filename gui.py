import random, main
from tkinter import *


def toonLoginFrame():
    """Toont de hoofdpagina en verbergt degene die open stond als er terug gegaan is"""
    nieuweKluisFrame.pack_forget()
    tijdFrame.pack_forget()
    kostenFrame.pack_forget()
    inleverenKluisFrame.pack_forget()
    loginframe.pack()

def toonNieuweKluisFrame():
    """Toont het frame voor het aanvragen van een nieuwe kluis en verbergt het hoofdframe"""
    loginframe.pack_forget()
    nieuweKluisFrame.pack()

def toonInleverenKluisFrame():
    """Toont het frame voor het inleveren van kluizen en verbergt het hoofdframe"""
    loginframe.pack_forget()
    inleverenKluisFrame.pack()

def toonTijdFrame():
    """Toont het frame voor het berekenen van gestalde tijd en verbergt het hoofdframe"""
    loginframe.pack_forget()
    tijdFrame.pack()

def toonKostenFrame():
    """Toont het frame om de kosten tot nu toe te berekenen en verbergt het hoofdframe"""
    loginframe.pack_forget()
    kostenFrame.pack()

def nummerGenerator():
    """Genereerd een random getal van 0 tot 25 om gescande kaarten te simuleren"""
    nummer = random.randrange(0, 25)
    return nummer

def kostenBerekenen():
    """Berekent de kosten van de opgegeven kaart als die een kluis in gebruik heeft"""
    nummer = kostenNummer.get()
    if main.intOVChek(nummer) == 'geenInt':
        kostenLabel["text"] = "Uw OV kaartnummer bestaat alleen uit cijfers."
    elif main.intOVChek(nummer) == 'negatief':
        kostenLabel["text"] = "U moet een OV kaartnummer opleveren, deze zijn niet negatief."
    elif main.intOVChek(nummer) == 'geenOV':
        kostenLabel["text"] = "Uw OV is niet in onze database gevonden."
    else:
        nummer = int(nummer)
        kosten = main.huidigePrijs(nummer)
        kostenLabel["text"] = kosten

def nieuweKluis():
    """Vraagt om een random gegenereerd getal, controleert of die al een kluis in gebruik heeft en geeft het kaartnummer en het bericht dat uit de functie komt weer"""
    nummer = nummerGenerator()
    nummer = int(nummer)
    resultaat = main.nieuweKluis(nummer)
    bericht = "Uw kaartnummer is: {}\n".format(nummer) + resultaat
    nieuweKluis["text"] = bericht

def inleverenKluis():
    """Vraagt om een kaartnummer die gecontroleerd wordt of die een kluis heeft. Als die een kluis heeft wordt de kluis verwijdert, anders gebeurd er niets, en wordt weergegeven wat er gebeurdt is"""
    nummer = inleverenKluisEntry.get()
    if main.intOVChek(nummer) == 'geenInt':
        inleverenLabel["text"] = "Uw OV kaartnummer bestaat alleen uit cijfers."
    elif main.intOVChek(nummer) == 'negatief':
        inleverenLabel["text"] = "U moet een OV kaartnummer opleveren, deze zijn niet negatief."
    elif main.intOVChek(nummer) == 'geenOV':
        inleverenLabel["text"] = "Uw OV is niet in onze database gevonden."
    else:
        nummer = int(nummer)
        inleverenLabel["text"] = 'U heeft uw kluisje {} ingeleverd'.format(main.kluisIndex(nummer))
        main.kluisInleveren(nummer)

def tijdBerekenen():
    """Berekent de verstreken tijd sinds er iets in een kluis is gezet door de kaartnummer"""
    nummer = tijdAanvraag.get()
    if main.intOVChek(nummer) == 'geenInt':
        inleveren = "Uw kaartnummer bestaat alleen uit cijfers."
        tijdLabel["text"] = inleveren
    elif main.intOVChek(nummer) == 'negatief':
        inleveren = "U moet een OV kaartnummer opleveren, deze zijn niet negatief."
        tijdLabel["text"] = inleveren
    elif main.intOVChek(nummer) == 'geenOV':
        inleveren = "Uw OV is niet in onze database gevonden."
        tijdLabel["text"] = inleveren
    else:
        nummer = int(nummer)
        minuten = main.stalTijd(nummer)
        minutenrest = minuten % 60
        uren = minuten // 60
        urenrest = uren % 24
        dagen = uren // 24
        tijdBericht = ""
        if dagen > 0:
            tijdBericht = 'uw fiets staat al {} dagen en {} uur gestalt.'.format(dagen, urenrest)
        elif uren > 0:
            tijdBericht = 'Uw fiets staat al {} uur en {} minuten gestalt'.format(uren, minutenrest)
        elif minuten < 60:
            tijdBericht = 'Uw fiets staat al {} minuten gestalt.'.format(minuten)
        if isinstance(minuten, str):
            tijdBericht = "U heeft geen kluis in gebruik\n"
            tijdLabel["text"] = tijdBericht
        else:
            bericht = tijdBericht + "Uw kaartnummer is: " + str(nummer)
            tijdLabel["text"] = bericht
        tijdLabel["text"] = tijdBericht


root = Tk()
root.geometry('500x300')
root.resizable(False,False)

"""Hoofdframe wordt aangemaakt met alle text, buttons en uiterlijk"""
loginframe = Frame(master=root, background='yellow')
loginframe.pack(fill="both", expand=True)
welkom = "Welkom bij de ov-staller"
welkomLabel = Label(master=loginframe, text=welkom, background='yellow')
welkomLabel.pack(pady=10)
nieuweKluisButton = Button(master=loginframe, text='Nieuwe kluis', command=toonNieuweKluisFrame, foreground="white", background="deep sky blue")
nieuweKluisButton.pack(side=LEFT, padx=10, pady=20)
inleverenKluisButton = Button(master=loginframe, text='Kluis inleveren', command=toonInleverenKluisFrame, foreground="white", background="deep sky blue")
inleverenKluisButton.pack(side=LEFT, padx=10, pady=20)
tijdButton = Button(master=loginframe, text="Bereken tijd", command=toonTijdFrame, foreground="white", background="deep sky blue")
tijdButton.pack(side=LEFT, padx=10, pady=20)
kostenButton = Button(master=loginframe, text="Bereken kosten", command=toonKostenFrame, foreground="white", background="deep sky blue")
kostenButton.pack(side=LEFT, padx=10, pady=20)
label = Label(master=loginframe, width=28, height=27, background='yellow')
label.pack()

"""Frame voor nieuwe kluis aanvragen wordt aangemaakt met alle knoppen, entries (overbodig door random generator) en tekst"""
nieuweKluisFrame = Frame(master=root, background='yellow')
nieuweKluisFrame.pack(fill="both", expand=True)
nummerField = Entry(master=nieuweKluisFrame)
nummerField.pack(pady=20)
kaartNummer = Button(master=nieuweKluisFrame, text='Volgende', command=nieuweKluis, foreground="white", background="deep sky blue")
kaartNummer.pack(pady=10)
backbutton = Button(master=nieuweKluisFrame, text='<', command=toonLoginFrame, foreground="white", background="deep sky blue")
backbutton.pack(padx=20, pady=20)
nieuweKluis = Label(master=nieuweKluisFrame, text="", width=80, height=20, background='yellow')
nieuweKluis.pack()

"""Frame voor het inleveren van kluizen wordt gemaakt met alle knoppen, tekst en entry"""
inleverenKluisFrame = Frame(master=root, background='yellow')
inleverenKluisFrame.pack(fill="both", expand=True)
vraag = "Welke kaartnummer is van u?"
vraagLabel = Label(master=inleverenKluisFrame, text=vraag, background='yellow')
vraagLabel.pack()
inleverenKluisEntry = Entry(master=inleverenKluisFrame)
inleverenKluisEntry.pack(pady=5)
inleverenKluisButton = Button(master=inleverenKluisFrame, text='Volgende', command=inleverenKluis, foreground="white", background="deep sky blue")
inleverenKluisButton.pack(pady=10)
backbutton = Button(master=inleverenKluisFrame, text='<', command=toonLoginFrame, foreground="white", background="deep sky blue")
backbutton.pack(padx=20, pady=20)
inleverenLabel = Label(master=inleverenKluisFrame, width=80, height=20, background='yellow')
inleverenLabel.pack(pady=10)

"""Frame voor het berekenen van de verlopen tijd wordt gemaakt met alle knoppen, tekst en entry"""
tijdFrame = Frame(master=root, background='yellow')
tijdFrame.pack(fill="both", expand=True)
vraag = "Wat is uw kaartnummer?"
label = Label(master=tijdFrame, text=vraag, background='yellow')
label.pack(pady=10)
tijdAanvraag = Entry(master=tijdFrame)
tijdAanvraag.pack(pady=5)
tijdAanvraagButton = Button(master=tijdFrame, text='Volgende', command=tijdBerekenen, foreground="white", background="deep sky blue")
tijdAanvraagButton.pack(pady=5)
backbutton = Button(master=tijdFrame, text='<', command=toonLoginFrame, foreground="white", background="deep sky blue")
backbutton.pack(padx=20, pady=20)
tijdLabel = Label(master=tijdFrame, text="", width=80, height=20, background='yellow')
tijdLabel.pack()

"""Frame voor het berekenen van de kosten wordt gemaakt met alle knoppen, tekst en entry"""
kostenFrame = Frame(master=root, background='yellow')
kosten = "Was is uw kaartnummer?"
kostenVraag = Label(master=kostenFrame, text=kosten, background='yellow')
kostenVraag.pack(pady=10)
kostenFrame.pack(fill="both", expand=True)
kostenNummer = Entry(master=kostenFrame)
kostenNummer.pack(pady=10)
nummerButton = Button(master=kostenFrame, text='Volgende', command=kostenBerekenen, foreground="white", background="deep sky blue")
nummerButton.pack(pady=20)
backbutton = Button(master=kostenFrame, text='<', command=toonLoginFrame, foreground="white", background="deep sky blue")
backbutton.pack(pady=20)
kostenLabel = Label(master=kostenFrame, text="", width=80, height=20, background='yellow')
kostenLabel.pack()

"""Main loop om de GUI te blijven runnen"""
toonLoginFrame()
root.mainloop()
