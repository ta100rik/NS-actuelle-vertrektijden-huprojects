from tkinter import *
import tkinter as tk


# nieuw venster voor vertrektijden
def vertrektijden():
    actueel = tk.Toplevel(root)
    actueel.title("Actuele vertrektijden")
    actueel.configure(bg='#ffc917')


    actueellabel = Label(master=actueel,
                         text="Actuele vertrektijden",
                         background='#ffc917',
                         foreground='#003082',
                         font=('NS Sans', 34, 'bold'))

    actueellabel.grid(row=0, column=2)

    utrechtlabel = Label(master=actueel,
                         text='Vertrektijden Utrecht Centraal',
                         background = '#ffc917',
                         foreground = '#003082',
                         font=('NS Sans', 16, 'bold'))
    utrechtlabel.grid(row=1)




    stationlabel= Label(master=actueel,
                        text='Van welk station wilt u \nde actuele vertrektijden? : ',
                        background='#ffc917',
                        foreground='#003082',
                        font=('NS Sans', 16, 'bold'))
    stationlabel.grid(row=2, column=2)

    amsterdam = Button(master=actueel,
                       text='Amsterdam',
                       font=('NS Sans', 14, 'bold'),
                       bg='#4B0082',
                       fg='white',
                       command=clicked,
                       height=5,
                       width=10)
    amsterdam.grid(row=1, column=4)




    entry = Entry(master=actueel)
    entry.grid(row=2,column=3)



# venster voor de niet gebruikte knoppen
def clicked():
    click = tk.Toplevel(root)
    click.title("Oops")
    click.configure(bg='#ffc917')
    click.geometry("800x600")

    labelclick = Label(master=click,
                       text='Wegens onderhoud is deze pagina niet beschikbaar,\nprobeert u het later nog eens',
                       background='#ffc917',
                       foreground='#003082',
                       font=('NS Sans', 21, 'bold'))
    labelclick.pack()

    # terugknop met een killfunctie
    terug = Button(master=click,
                   text='Terug naar hoofdscherm',
                   font=('NS Sans', 18, 'bold'),
                   bg='#4B0082',
                   fg='white',
                   command=click.destroy)
    terug.pack(pady=10)


root = Tk()  # Creëer het hoofdschermroot.

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

# De knoppen
button1 = Button(master=root,
                 text='Ik wil naar \nAmsterdam',
                 font=('NS Sans', 14, 'bold'),
                 bg='#4B0082',
                 fg='white',
                 command=clicked)
button1.pack(pady=10)

button2 = Button(master=root,
                 text='Kopen los \nkaartje',
                 font=('NS Sans', 14, 'bold'),
                 bg='#4B0082',
                 fg='white',
                 command=clicked)
button2.pack(pady=10)

button3 = Button(master=root,
                 text='Kopen \nOV-Chipkaart',
                 font=('NS Sans', 14, 'bold'),
                 bg='#4B0082',
                 fg='white',
                 command=clicked)
button3.pack(pady=10)

button4 = Button(master=root,
                 text='Ik wil naar \nhet Buitenland',
                 font=('NS Sans', 14, 'bold'),
                 bg='#4B0082',
                 fg='white',
                 command=clicked)
button4.pack(pady=10)

button5 = Button(master=root,
                 text='Actuele \nvertrektijden',
                 font=('NS Sans', 14, 'bold'),
                 bg='#4B0082',
                 fg='white',
                 command=vertrektijden)
button5.pack(pady=10)

root.mainloop()  # Toon het hoofdscherm
