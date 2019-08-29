
import random
from random import shuffle


class Kviz:
    def __init__(self):
        self.ime = input('Vaše ime: ')
        self.pozdrav = print('Pozdravljeni, ' + self.ime )
        self.navodila = print('Najprej boste izbrali temo za kviz izbirate lahko med nogometom, košarko in slovenskim športom.'
                              'Kviz rešujete tako, da pri vsakem vprašanju izberete enega od treh odgovorov (a, b ali c).')
        self.izbor = None
        self.pravilnih = 0

#Nabor vprašanj in odgovorv iz vsake teme bomo predstavili s seznamom slovarjev

Nogomet = [
        {vprasanje : 'Proti kateri reprezentanci je Diego Maradona dosegel gol z roko ("Božja roka")? ',
         'a': 'Nemčija', 'b' : 'Anglija',  'c' : 'Brazilija', odgovor : 'b'},
        {vprasanje : 'Kateri angleški klub je večkrat osvojil ligo prvakov kot pa domače prvenstvo? ',
         'a' : 'Nottingham Forest', 'b' : 'Chelsea', 'c' :  'Aston Villa', odgovor : 'a'},
        {vprasanje : 'Nogometaši Chieva Verona imajo zelo nenavaden vzdevek, in sicer:'
         'a': 'Rumena podmornica', 'b' : 'Leteči oslički',  'c' :  'Karamele', odgovor : 'b'}
        ]
       
Kosarka = [
        {vprasanje : 'Največkrat (petkrat) so svetovni prvaki reprezentanci ZDA in: ',
         'a' : 'Španija', 'b' : 'Sovjetska zveza', 'c' : 'Jugoslavija', odgovor : 'c'},
        {vprasanje : 'Na olimpijskih igrah leta 1992 so ameriško reprezentanco poimenovali kar: ',
         'a' : 'Fantasy team', 'b' : 'Dream team',  'c' :  'All star team', odgovor : 'b'},
        {vprasanje : 'Kobe Bryant je bil na naboru za ligo NBA izbran šele kot: ',
         'a' :  '13.', 'b' :  '4.',  'c' :  '20.', odgovor : 'a'}
        ]

Slo_sport = [
        {vprasanje : 'Koliko medalj je Slovenija osvojila na olimpijskih igrah v Sočiju leta 2014? ',
         'a' :  '8',  'b' : '6', 'c' : '3', odgovor : 'a'},
        {vprasanje : 'Kateri od naštetih smučarskih skakalcev ni nikoli dobil ocene za slog 5-krat 20?',
         'a' : 'Peter Prevc', 'b' : 'Jurij Tepeš', 'c' : 'Primož Peterka', odgovor : 'c'},
        {vprasanje : 'Kljub temu da je bil Leon Štukelj izjemen gimnastik, pa je tudi dokončal študij: ',
        'a' : 'Fizike', 'b' : 'Prava', 'c' : 'Medicine', odgovor : 'b'}
        ]
                   
def tema(self):
    self.izbor = input('Izberite temo, vnesite 1, 2 ali 3: \n 1)Nogomet \n 2) Košarka \n 3) Slovenski šport \n Tema: ')
    if self.izbor == '1':
        tema = Nogomet
    elif self.izbor == '2':
        tema = Kosarka
    elif self.izbor == '3':
        tema = Slo_sport
    else:
        input('Temo lahko izberete le tako, da vnesete 1, 2 ali 3: ')

def preveri(tema, odg, k):
    pravilen_odgovor = tema[k].get(odgovor)
    if odg == pravilen_odgovor:
        self.pravilnih += 1
        print('odgovor je pravilen!')
    else:
        print('Odgovor ni pravilen, pravilen odgovor je {}.'.format(pravilen_odgovor) )

def izvedi(sez):
    k = 0 #Štejemo vprašanja
    while k < 3:
        print(sez[k].get[vprasanje])
        print('a' + sez[k].get['a'])
        print('b' + sez[k].get['b'])
        print('c' + sez[k].get['c'])
        odg = input('Odgovor je: ')
        if odg not in 'abc':
            odg = input('Odgovorite lahko le tako da vnesete a, b ali c, torej odgovor je: ')
        preveri(tema, odg, k)
        k += 1
    print('Prišli ste do konca {}, pravilno ste odgovorili na {} vprašanj od treh'.format(self.ime, self.pravilnih))

kviz = Kviz()
tema(kviz)



    
 



               
