
from tkinter import *
import random

with open('vprašanja.txt' , 'w') as dat:
    print('Na prvem svetovnem prvenstvu leta 1930 so vse tekme potekale v:;Montevideu;Sao Paolu;Beogradu \n'
          'Največ zadetkov na enem prvenstvu, kar 13 je zadel:;Just Fontaine(Francija);Pele(Brazilija);Gerd Müller(Nemčija)\n'
          'Najhitrejši zadetek je leta 2002 zadel Hakan Sükur, zanj je potreboval:;11 sekund;32 sekund;5 sekund\n'
          'Katera reprezentanca je nazadnje kot gostitelj osvojila prvenstvo?;Francija;Argentina;Nemčija\n'
          'Katera reprezentanca je že trikrat igrala v finalu in še ni postala svetovni prvak?;Nizozemska;Madžarska;Portugalska\n'
          'Na prvenstvu leta 1986 je v četrtfinalu Diego Maradona zadel enega od svojih 2 zadetkov z roko znan je kot božja roka. Proti komu?;Anglija;Brazilija;Čile\n'
          'Največ zadetkov na vseh prvenstvih skupaj (16) je zadel:;Miroslav Klose;Pele;Just Fontaine\n'
          'Na poti do naslova svetovnega prvaka leta 2006 je Italija tako v kvalifikacijah kot na prvenstu izgubala zgolj proti:;Sloveniji;ZDA;Norveški\n'
          'Kdo je edini, nogometaš, ki je v finalu svetovnega prvenstva zadel trikrat?;Geoff Hurst;Diego Maradona;Ronaldo\n'
          'Samo dvem ekipam je uspelo obraniti naslov svetovnega prvaka, to sta:;Italija in Brazilija;Nemčija in Francija;Brazilija in Nemčija\n'
          'Na svetovnem prvenstvu se še nikoli ni zgodilo, da bi:;Zmagovalce vodil tuj selektor;Domačin izpadel po skupinskem delu;Finale igrali dve neevropski ekipi\n'
          'Zadnja trije prvaki (Španija, Italija, Nemčija) so na prvenstvu, kjer so branili naslov:;Izpadli po skupinskem delu;Izpadli v četrtfinalu;Izgubili proti kasnejšemu prvaku\n'
          'Na SP v Rusiji sta prvič nastopili:;Islandija in Panama;Tunizija in Peru;Islandija in Egipt\n'
          'Za edino slovensko zmago na svetovnih prvenstvih (1:0 nad Alžirijo) je edini gol zadel:;Robert Koren;Milivoje Novakovič;Zlatko Zahovič\n'
          'Kolikokrat se je zgodilo, da finalna tekma ni bila odigrana v glavnem mestu države gostiteljice?;5;2;3\n'
          , file=dat)



class Kviz:
    def __init__(self, okno):
        self.navodila = Label(okno, text='Pozdravljeni v kvizu o zgodovini svetovnih'
               ' prvenstev v nogometu. Kviz rešujete tako, da pri vsakem vprašanju '
               'izberete enega od treh odgovorov.')
        self.navodila.grid(row=0, column=0, columnspan=3)

        self.zacetek = Button(okno, text='Začni kviz', command=zacnimo)

        self.odgovor = Label(okno, text='')
        
        self.pravilnih = 0

        
def preberi_vprasanja():
    with open('vprašanja.txt', 'r') as dat:
        prebrano = []
        for vrstica in dat:
            nabor = vrstica.strip().split(';')
            nabor = tuple(nabor)
            prebrano.append(nabor)
    print(prebrano)
        


def izbira_vprasanj():
    izbrana_vprasanja = []
    while len(izbrana_vprasanja) < 5:
        x = random.randint(0, 14)
        if x not in izbrana_vprasanja:
            izbrana_vprasanja.append(x)
    print(izbrana_vprasanja)




def vprasanje_in_odgovori(self, okno):
    izbira_vprasanj()
    #for x in izbrana_vprasanja:
        #prebrano[x] = 
        
        
    vprasanje = Label(okno, text='Na prvem svetovnem prvenstvu leta 1930 v Urugvaju'
                      ' je prvak postata reprezentanca:')
    A = Button(okno, text='Urugvaj', command=pravilno)
    B = Button(okno, text='Brazilija', command=napacno)
    C = Button(okno, text='Jugoslavija in srbija in še nekej', command=napacno)

    vprasanje.grid(row=0, column=0, columnspan=3)
    A.grid(row=1, column=0)
    B.grid(row=1, column=1)
    C.grid(row=1, column=2)

    


def pravilno():
    kviz.odgovor = Label(okno, text='Pravilno')
    kviz.odgovor.grid(row=2, column=0)
    kviz.pravilnih += 1
    Naslednje = Button(okno, text='Naslednje vprašanje')
    Naslednje.grid(row=2, column=2)
    


def napacno():
    kviz.odgovor  = Label(okno, text='Narobe')
    kviz.odgovor.grid(row=2, column=0)
    Naslednje = Button(okno, text='Naslednje vprašanje')
    Naslednje.grid(row=2, column=2)


def zacnimo():
    kviz.navodila.destroy()
    kviz.zacetek.destroy()
    vprasanje_in_odgovori(kviz, okno)

    
 
okno = Tk()
kviz = Kviz(okno)


kviz.zacetek.grid(row=1, column=0)

okno.mainloop()


               
