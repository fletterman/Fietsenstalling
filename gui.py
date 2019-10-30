import kluisje
from tkinter import *

# kluisje.kluisjecheck(2, 4)
# runt kluisjecheck functie uit file kluisje.py

def clicked():
    bericht = 'Dit een bericht voor de gebruiker!'
    showinfo(title='popup', message=bericht)

#Hiertussen stonden alle functies

root = Tk()
button = Button(master=root, text='Druk hier', command=clicked)
button.pack(pady=10)

root.mainloop()