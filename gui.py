import random, main
from tkinter import *


# Toont de hoofdpagina en verbergt degene die open stond als er terug gegaan is
def toonLoginFrame():
    nieuweKluisFrame.pack_forget()
    tijdFrame.pack_forget()
    kostenFrame.pack_forget()
    inleverenKluisFrame.pack_forget()
    loginframe.pack()

# Toont het frame voor het aanvragen van een nieuwe kluis en verbergt het hoofdframe
def toonNieuweKluisFrame():
    loginframe.pack_forget()
    nieuweKluisFrame.pack()

# Toont het frame voor het inleveren van kluizen en verbergt het hoofdframe
def toonInleverenKluisFrame():
    loginframe.pack_forget()
    inleverenKluisFrame.pack()

# Toont het frame voor het berekenen van gestalde tijd en verbergt het hoofdframe
def toonTijdFrame():
    loginframe.pack_forget()
    tijdFrame.pack()

# Toont het frame om de kosten tot nu toe te berekenen en verbergt het hoofdframe
def toonKostenFrame():
    loginframe.pack_forget()
    kostenFrame.pack()

# Genereerd een random getal van 0 tot 25 om gescande kaarten te simuleren
def nummerGenerator():
    nummer = random.randrange(0, 25)
    return nummer

# Berekent de kosten van de opgegeven kaart als die een kluis in gebruik heeft
def kostenBerekenen():
    nummer = kostenNummer.get()
    if isinstance(nummer, str):
        inleveren = "Geef een cijfer als je kaartnummer en niet een string"
        kostenLabel["text"] = inleveren
    else:
        nummer = int(nummer)
        kosten = main.huidigePrijs(nummer)
        kostenLabel["text"] = kosten

# Vraagt om een random gegenereerd getal, controleert of die al een kluis in gebruik heeft en geeft het kaartnummer en het bericht dat uit de functie komt weer
def nieuweKluis():
    nummer = nummerGenerator()
    nummer = int(nummer)
    resultaat = main.nieuweKluis(nummer)
    bericht = "Uw kaartnummer is: {}\n".format(nummer) + resultaat
    nieuweKluis["text"] = bericht

# Vraagt om een kaartnummer die gecontroleerd wordt of die een kluis heeft. Als die een kluis heeft wordt de kluis verwijdert, anders gebeurd er niets, en wordt weergegeven wat er gebeurdt is
def inleverenKluis():
    nummer = inleverenKluisEntry.get()
    if isinstance(nummer, str):
        inleveren = "Geef een cijfer als je kaartnummer en niet een string"
        inleverenLabel["text"] = inleveren
    else:
        nummer = int(nummer)
        inleveren = main.kluisInleveren(nummer)
        inleverenLabel["text"] = inleveren

# Berekent de verstreken tijd sinds er iets in een kluis is gezet door de kaartnummer
def tijdBerekenen():
    nummer = tijdAanvraag.get()
    if isinstance(nummer, str):
        inleveren = "Geef een cijfer als je kaartnummer en niet een string"
        tijdLabel["text"] = inleveren
    else:
        nummer = int(nummer)
        minuten = main.stalTijd(nummer)
        minutenrest = minuten % 60
        uren = minuten // 60
        urenrest = uren % 24
        dagen = uren // 24
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

root = Tk()

# Hoofdframe wordt aangemaakt met alle text, buttons en uiterlijk
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

# Frame voor nieuwe kluis aanvragen wordt aangemaakt met alle knoppen, entries (overbodig door random generator) en tekst
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

# Frame voor het inleveren van kluizen wordt gemaakt met alle knoppen, tekst en entry
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

# Frame voor het berekenen van de verlopen tijd wordt gemaakt met alle knoppen, tekst en entry
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

# Frame voor het berekenen van de kosten wordt gemaakt met alle knoppen, tekst en entry
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

# Main loop om de GUI te blijven runnen
toonLoginFrame()
root.mainloop()
