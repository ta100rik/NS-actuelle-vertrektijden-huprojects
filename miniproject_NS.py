import requests
import xmltodict
# import ns_api
from tkinter import *
import tkinter as tk


def api_request(station):
    auth_details = ('Farhad_sayghani@msn.com', 'r_MptU5smHBzB5wKFjw5q76-_6JVo1U9JU-PriJLYZnj4XnBfI7a7A')
    api_url = 'http://webservices.ns.nl/ns-api-avt?station=' + station
    response = requests.get(api_url, auth=auth_details)

    vertrekXML = xmltodict.parse(response.text)
    lijst = []
    for vertrek in vertrekXML['ActueleVertrekTijden']['VertrekkendeTrein']:
        eindbestemming = vertrek['EindBestemming']
        spoor = vertrek['VertrekSpoor']['#text']
        vertrektijd = vertrek['VertrekTijd']  # 2016-09-27T18:36:00+0200
        vertrektijd = vertrektijd[11:16]  # 18:36
        lijst.append([vertrektijd,eindbestemming,spoor])
        # print('Om ' + vertrektijd + ' vertrekt een trein naar ' + eindbestemming)
    return lijst

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


def clicked2(userinput):
    vertrektijden = api_request(userinput)
    click2 = tk.Toplevel(root)
    click2.title('Actuele vertrektijden')
    click2.configure(bg='#ffc917')
    click2.geometry("800x600")

    topframe = Frame(master=click2,
                     bg='#ffc917',
                     width=800,
                     height=50,
                     pady=3)
    centerframe = Frame(master=click2,
                        bg='#ffc917')
    bottomframe = Frame(master=click2,
                        bg='#ffc917')

    # layout van de main containers
    click2.grid_rowconfigure(1, weight=1)
    click2.grid_columnconfigure(0, weight=1)

    topframe.grid(row=0, sticky="ew")
    centerframe.grid(row=1, sticky="nsew")
    bottomframe.grid(row=2, sticky='ew')

    labelclick = Label(master=topframe,
                       text='Actuele Vertrektijd - ' + str(userinput),
                       background='#ffc917',
                       foreground='#003082',
                       font=('NS Sans', 21, 'bold'))
    labelclick.grid(row=0, column=1)

    counter = 2
    first = 0
    second = 1
    third = 2
    for vertrektijd in vertrektijden:
        tijd = vertrektijd[0]
        station = vertrektijd[1]
        spoor = vertrektijd[2]
        resultLabel = Label(master=centerframe, text=station)
        resultLabel2 = Label(master=centerframe, text=spoor)
        resultLabel3 = Label(master=centerframe, text=tijd)
        resultLabel.grid(row=counter, column=first)
        resultLabel2.grid(row=counter, column=second)
        resultLabel3.grid(row=counter, column=third)
        counter = 1 + counter
        if counter == 20:
            counter = 2
            first = first + 3
            second = second + 3
            third = third + 3

    # terugknop met een killfunctie
    terug = Button(master=bottomframe,
                   text='Terug',
                   font=('NS Sans', 18, 'bold'),
                   bg='#4B0082',
                   fg='white',
                   command=click2.destroy)
    terug.grid(row=0, column=2)


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

    actueellabel.grid(row=0, column=2, columnspan=4, sticky='nsew')



    stationlabel = Label(master=topframe,
                         text='Van welk station wilt u \nde actuele vertrektijden?',
                         background='#ffc917',
                         foreground='#003082',
                         font=('NS Sans', 16, 'bold'))
    stationlabel.grid(row=1, column=0, sticky='nsew')

    # Center widgets
    centerframe.grid_rowconfigure(0, weight=1)
    centerframe.grid_columnconfigure(1, weight=1)

   # ctr_left = Frame(centerframe, bg='#ffc917')
    ctr_mid = Frame(centerframe, bg='#ffc917')
    ctr_right = Frame(centerframe, bg='#ffc917')

    #ctr_left.grid(row=0, column=0, sticky="nw")
    ctr_mid.grid(row=0, column=1, sticky="nsew")
    ctr_right.grid(row=0, column=2, sticky="nw")


    # Entry voor het invoeren van gekozen station

    utrechtlabel = Label(master=ctr_mid,
                         text='Vertrektijden - Utrecht Centraal',
                         background='#ffc917',
                         foreground='#003082',
                         font=('NS Sans', 16, 'bold'))
    utrechtlabel.grid(row=0, column=0, sticky='nsew')

    entrylabel = Label(master=topframe,
                       text='Voer uw stad in: ',
                       bg='#ffc917',
                       fg='#003082',
                       font=('NS Sans', 11, 'bold'))
    entrylabel.grid(row=2, column=0)

    station = StringVar()
    mijnInvoer = Entry(master=topframe, textvariable=station)
    mijnInvoer.focus()
    mijnInvoer.bind("<Return>")
    mijnInvoer.grid(row=2, column=1)
    # Enter knop
    enterEntry = Button(topframe, text='Zoeken',
                        font=('NS Sans', 12, 'bold'),
                        bg='#4B0082',
                        fg='white',
                        command=lambda: clicked2(mijnInvoer.get()))
    enterEntry.grid(row=2, column=2)

    resultLabel = Label(master=ctr_mid, text="Result:sdfsdgdasfdgdfgfd ")
    resultLabel.grid(row=1, column=0, rowspan=3, columnspan=3)

    # Right widgets

    # Knoppen voor de steden
    amsterdam = Button(master=ctr_right,
                       text='Amsterdam',
                       font=('NS Sans', 12, 'bold'),
                       bg='#4B0082',
                       fg='white',
                       command=lambda:clicked2('Amsterdam'),
                       height=3,
                       width=10)
    amsterdam.grid(row=0, column=0)

    rotterdam = Button(master=ctr_right,
                       text='Rotterdam',
                       font=('NS Sans', 12, 'bold'),
                       bg='#4B0082',
                       fg='white',
                       command=lambda:clicked2('Rotterdam'),
                       height=3,
                       width=10)
    rotterdam.grid(row=0, column=1)

    arnhem = Button(master=ctr_right,
                    text='Arnhem',
                    font=('NS Sans', 12, 'bold'),
                    bg='#4B0082',
                    fg='white',
                    command=lambda:clicked2('Arnhem'),
                    height=3,
                    width=10)
    arnhem.grid(row=1, column=0)

    utrecht = Button(master=ctr_right,
                     text='Utrecht',
                     font=('NS Sans', 12, 'bold'),
                     bg='#4B0082',
                     fg='white',
                     command=lambda:clicked2('Utrecht'),
                     height=3,
                     width=10)
    utrecht.grid(row=1, column=1)

    maastricht = Button(master=ctr_right,
                        text='Maastricht',
                        font=('NS Sans', 12, 'bold'),
                        bg='#4B0082',
                        fg='white',
                        command=lambda:clicked2('Maastricht'),
                        height=3,
                        width=10)
    maastricht.grid(row=2, column=0)

    hertogenbosch = Button(master=ctr_right,
                           text='\'s-Hertogen\n-bosch',
                           font=('NS Sans', 12, 'bold'),
                           bg='#4B0082',
                           fg='white',
                           command=lambda:clicked2('\'s-Hertogenbosch'),
                           height=3,
                           width=10)
    hertogenbosch.grid(row=2, column=1)

    lelystad = Button(master=ctr_right,
                      text='Almere',
                      font=('NS Sans', 12, 'bold'),
                      bg='#4B0082',
                      fg='white',
                      command=lambda:clicked2('Almere'),
                      height=3,
                      width=10)
    lelystad.grid(row=3, column=0)

    zwolle = Button(master=ctr_right,
                    text='Zwolle',
                    font=('NS Sans', 12, 'bold'),
                    bg='#4B0082',
                    fg='white',
                    command=lambda:clicked2('Zwolle'),
                    height=3,
                    width=10)
    zwolle.grid(row=3, column=1)

    assen = Button(master=ctr_right,
                   text='Assen',
                   font=('NS Sans', 12, 'bold'),
                   bg='#4B0082',
                   fg='white',
                   command=lambda:clicked2('Assen'),
                   height=3,
                   width=10)
    assen.grid(row=4, column=0)

    groningen = Button(master=ctr_right,
                       text='Groningen',
                       font=('NS Sans', 12, 'bold'),
                       bg='#4B0082',
                       fg='white',
                       command=lambda: clicked2('Groningen'),
                       height=3,
                       width=10)
    groningen.grid(row=4, column=1)

    leeuwarden = Button(master=ctr_right,
                        text='Leeuwarden',
                        font=('NS Sans', 12, 'bold'),
                        bg='#4B0082',
                        fg='white',
                        command=lambda:clicked2('Leeuwarden'),
                        height=3,
                        width=10)
    leeuwarden.grid(row=5, column=0)

    denhaag = Button(master=ctr_right,
                     text='Den Haag',
                     font=('NS Sans', 12, 'bold'),
                     bg='#4B0082',
                     fg='white',
                     command=lambda:clicked2('Den Haag'),
                     height=3,
                     width=10)
    denhaag.grid(row=5, column=1)

    middelburg = Button(master=ctr_right,
                        text='Middelburg',
                        font=('NS Sans', 12, 'bold'),
                        bg='#4B0082',
                        fg='white',
                        command=lambda: clicked2('Middelburg'),
                        height=3,
                        width=10)
    middelburg.grid(row=6, column=0)

    haarlem = Button(master=ctr_right,
                     text='Haarlem',
                     font=('NS Sans', 12, 'bold'),
                     bg='#4B0082',
                     fg='white',
                     command=lambda: clicked2('Haarlem'),
                     height=3,
                     width=10)
    haarlem.grid(row=6, column=1)


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
