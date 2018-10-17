from tkinter import *

def toonHoofdscherm():
    hoofdscherm.pack_forget()
    button1frame.pack()

def toonButton1():
    button1frame.pack_forget()
    hoofdscherm.pack()

def clicked():
    label['text'] = entry.get()







root = Tk()               # Creëer het hoofdschermroot.

hoofdscherm = Frame(master=root)
hoofdscherm.pack(fill='both', expand=True)
root.title('NS')
root.configure(background='#ffc917')
root.geometry('800x600')

label = Label(master=root,
              text='Welkom bij NS',
              background='#ffc917',
              foreground='#003082',
              font=('NS Sans', 34, 'bold'),
              width=14,
              height=3)
label.pack()

        #De knoppen
button1 = Button(master=root, text='Ik wil naar Amsterdam', background='#4B0082', command=clicked)
button1.pack(pady=10)

button2 = Button(master=root, text='Kopen Los kaartje', command=clicked)
button2.pack(pady=10)

button3 = Button(master=root, text='Kopen OV-Chipkaart', command=clicked)
button3.pack(pady=10)

button4 = Button(master=root, text='Ik wil naar het Buitenland', command=clicked)
button4.pack(pady=10)

button5 = Button(master=root, text='Actuele vertrektijden', background='#4B0082', command=clicked)
button5.pack(pady=10)

#   Venster 1
button1frame = Frame(master=root)
button1frame.pack(fill='both', expand=True)


backbutton = Button(master=button1frame, text='Terug', command=toonHoofdscherm)
backbutton.pack(padx=20, pady=20)

#   Venster 2
button1frame = Frame(master=root)
button1frame.pack(fill='both', expand=True)

#   Venster 3
button1frame = Frame(master=root)
button1frame.pack(fill='both', expand=True)

#   Venster 4
button1frame = Frame(master=root)
button1frame.pack(fill='both', expand=True)

button1frame = Frame(master=root)
button1frame.pack(fill='both', expand=True)
root.mainloop()                # Toon het hoofdscherm
