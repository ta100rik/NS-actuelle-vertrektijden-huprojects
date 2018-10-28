import requests
import xmltodict
from tkinter import *
import tkinter as tk

def api_request():
    auth_details = ('Farhad_sayghani@msn.com', 'r_MptU5smHBzB5wKFjw5q76-_6JVo1U9JU-PriJLYZnj4XnBfI7a7A')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=ut'
    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)
    print('Dit zijn de vertrekkende treinen:')

    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']

        vertrektijd = vertrek['VertrekTijd']      # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16]          # 18:36

        print('Om '+vertrektijd+' vertrekt een trein naar '+ eindbestemming)

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

def clicked2():
    click2 = tk.Toplevel(root)
    click2.title("Oops")
    click2.configure(bg='#ffc917')
    click2.geometry("800x600")

    labelclick = Label(master=click2,
                       text='Actuele Vertrektijd',
                       background='#ffc917',
                       foreground='#003082',
                       font=('NS Sans', 21, 'bold'))
    labelclick.pack()

    # terugknop met een killfunctie
    terug = Button(master=click2,
                   text='Terug',
                   font=('NS Sans', 18, 'bold'),
                   bg='#4B0082',
                   fg='white',
                   command=click2.destroy)
    terug.pack(side=BOTTOM, pady=10)


# nieuw venster voor vertrektijden
def vertrektijden():

    actueel = tk.Toplevel(root)
    actueel.title("Actuele vertrektijden")
    actueel.configure(bg='#ffc917')
    actueel.geometry('{}x{}'.format(1080, 700))

    # main containers
    topframe = Frame(master=actueel,
                     bg='#ffc917',
                     width=800,
                     height=50,
                     pady=3)
    centerframe = Frame(master=actueel,
                        bg='#ffc917')

    # layout van de main containers
    actueel.grid_rowconfigure(1, weight=1)
    actueel.grid_columnconfigure(0, weight=1)

    topframe.grid(row=0, sticky="ew")
    centerframe.grid(row=1, sticky="nsew")

    # Top widgets

    actueellabel = Label(master=topframe,
                         text="Actuele vertrektijden",
                         background='#ffc917',
                         foreground='#003082',
                         font=('NS Sans', 34, 'bold'))

    actueellabel.grid(row=0, column=1)

    utrechtlabel = Label(master=topframe,
                         text='Vertrektijden Utrecht Centraal',
                         background='#ffc917',
                         foreground='#003082',
                         font=('NS Sans', 16, 'bold'))
    utrechtlabel.grid(row=1, column=0)

    stationlabel = Label(master=topframe,
                         text='Van welk station wilt u \nde actuele vertrektijden?',
                         background='#ffc917',
                         foreground='#003082',
                         font=('NS Sans', 16, 'bold'))
    stationlabel.grid(row=1, column=1)

    # Center widgets
    centerframe.grid_rowconfigure(0, weight=1)
    centerframe.grid_columnconfigure(1, weight=1)

    ctr_left = Frame(centerframe, bg='white')
    ctr_mid = Frame(centerframe, bg='yellow')
    ctr_right = Frame(centerframe, bg='green')

    ctr_left.grid(row=0, column=0, sticky="ns")
    ctr_mid.grid(row=0, column=1, sticky="nsew")
    ctr_right.grid(row=0, column=2, sticky="ns")

    """def returnEntry():
        result = mijnInvoer.get()
        resultLabel.config(text=result)
        mijnInvoer.delete(0, END)"""


    # Entry voor het invoeren van gekozen station

    entrylabel = Label(master=ctr_mid,
                       text='Voer uw stad in: ',
                       bg='#ffc917',
                       fg='#003082',
                       font=('NS Sans', 11, 'bold'))
    entrylabel.grid(row=0, column=0)

    station = StringVar()
    mijnInvoer = Entry(master=ctr_mid, textvariable=station)
    mijnInvoer.focus()
    mijnInvoer.bind("<Return>")
    mijnInvoer.grid(row=0, column=1)


    #Enter knop
    enterEntry=Button(ctr_mid, text='Zoeken',
                      font=('NS Sans', 12, 'bold'),
                      bg='#4B0082',
                      fg='white',
                      command=clicked2)
    enterEntry.grid(row=0, column=2)



    resultLabel= Label(master=ctr_left, text="rteyhdrhdfgh")
    resultLabel.grid(row=0, rowspan=3)



    # Right widgets


    # Knoppen voor de steden
    amsterdam = Button(master=ctr_right,
                       text='Amsterdam',
                       font=('NS Sans', 12, 'bold'),
                       bg='#4B0082',
                       fg='white',
                       command=clicked,
                       height=3,
                       width=10)
    amsterdam.grid(row=2, column=4)

    rotterdam = Button(master=ctr_right,
                       text='Rotterdam',
                       font=('NS Sans', 12, 'bold'),
                       bg='#4B0082',
                       fg='white',
                       command=clicked,
                       height=3,
                       width=10)
    rotterdam.grid(row=3, column=4)

    arnhem = Button(master=ctr_right,
                    text='Arnhem',
                    font=('NS Sans', 12, 'bold'),
                    bg='#4B0082',
                    fg='white',
                    command=clicked,
                    height=3,
                    width=10)
    arnhem.grid(row=2, column=5)

    utrecht = Button(master=ctr_right,
                     text='Utrecht',
                     font=('NS Sans', 12, 'bold'),
                     bg='#4B0082',
                     fg='white',
                     command=clicked,
                     height=3,
                     width=10)
    utrecht.grid(row=3, column=5)

    maastricht = Button(master=ctr_right,
                        text='Maastricht',
                        font=('NS Sans', 12, 'bold'),
                        bg='#4B0082',
                        fg='white',
                        command=ctr_right,
                        height=3,
                        width=10)
    maastricht.grid(row=4, column=4)

    hertogenbosch = Button(master=ctr_right,
                           text='\'s-Hertogen\n-bosch',
                           font=('NS Sans', 12, 'bold'),
                           bg='#4B0082',
                           fg='white',
                           command=clicked,
                           height=3,
                           width=10)
    hertogenbosch.grid(row=4, column=5)

    lelystad = Button(master=ctr_right,
                      text='Lelystad',
                      font=('NS Sans', 12, 'bold'),
                      bg='#4B0082',
                      fg='white',
                      command=clicked,
                      height=3,
                      width=10)
    lelystad.grid(row=5, column=4)

    zwolle = Button(master=ctr_right,
                    text='Zwolle',
                    font=('NS Sans', 12, 'bold'),
                    bg='#4B0082',
                    fg='white',
                    command=clicked,
                    height=3,
                    width=10)
    zwolle.grid(row=5, column=5)

    assen = Button(master=ctr_right,
                   text='Assen',
                   font=('NS Sans', 12, 'bold'),
                   bg='#4B0082',
                   fg='white',
                   command=clicked,
                   height=3,
                   width=10)
    assen.grid(row=6, column=4)

    groningen = Button(master=ctr_right,
                       text='Groningen',
                       font=('NS Sans', 12, 'bold'),
                       bg='#4B0082',
                       fg='white',
                       command=clicked,
                       height=3,
                       width=10)
    groningen.grid(row=6, column=5)

    leeuwarden = Button(master=ctr_right,
                        text='Leeuwarden',
                        font=('NS Sans', 12, 'bold'),
                        bg='#4B0082',
                        fg='white',
                        command=clicked,
                        height=3,
                        width=10)
    leeuwarden.grid(row=7, column=4)

    denhaag = Button(master=ctr_right,
                     text='Den Haag',
                     font=('NS Sans', 12, 'bold'),
                     bg='#4B0082',
                     fg='white',
                     command=clicked,
                     height=3,
                     width=10)
    denhaag.grid(row=7, column=5)

    middelburg = Button(master=ctr_right,
                        text='Middelburg',
                        font=('NS Sans', 12, 'bold'),
                        bg='#4B0082',
                        fg='white',
                        command=clicked,
                        height=3,
                        width=10)
    middelburg.grid(row=8, column=4)

    haarlem = Button(master=ctr_right,
                     text='Haarlem',
                     font=('NS Sans', 12, 'bold'),
                     bg='#4B0082',
                     fg='white',
                     command=clicked,
                     height=3,
                     width=10)
    haarlem.grid(row=8, column=5)



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
