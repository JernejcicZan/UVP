

class Kviz:
    def __init__(self):
        self.ime = input('Vaše ime: ')
        self.pozdrav = print('Pozdravljeni, ' + self.ime + '.')
        self.navodila = print('Najprej boste izbrali temo za kviz. Izbirate lahko med nogometom, košarko in slovenskim športom. '
                              'Kviz rešujete tako, da pri vsakem vprašanju izberete enega od treh odgovorov (a, b ali c).')
        self.izbor = None
        self.pravilnih = 0


#Vprašanja za vsako temo zapišemo v datoteke
        
with open('Nogomet.txt', 'w') as d:
    d.write('Proti kateri reprezentanci je Diego Maradona dosegel gol z roko ("Božja roka")?; Nemčija; Anglija; Brazilija;b\n')
    d.write('Kateri angleški klub je večkrat osvojil ligo prvakov kot pa domače prvenstvo?; Nottingham Forest; Chelsea; Aston Villa;a\n')
    d.write('Nogometaši Chieva Verona imajo zelo nenavaden vzdevek, in sicer: ; Rumena podmornica; Leteči oslički; Karamele;b')

with open('Kosarka.txt', 'w') as d:
    d.write('Največkrat (petkrat) so svetovni prvaki v košarki postali reprezentanci ZDA in: ;Španija;Sovjetska zveza;Jugoslavija;c\n')
    d.write('Na olimpijskih igrah leta 1992 so ameriško reprezentanco poimenovali kar:;Fantasy team; Dream team; All star team;b\n')
    d.write('Kobe Bryant je bil na naboru za ligo NBA leta 1996 izbran kot; 13; 4; 20;a')

with open('Slo_sport.txt', 'w') as d:
    d.write('Koliko medalj je Slovenija osvojila na olimpijskih igrah v Sočiju leta 2014?; 8; 6; 3;a\n')
    d.write('Kateri od naštetih smučarskih skakalcev ni nikoli dobil ocene za slog 5-krat 20?; Peter Prevc; Jurij Tepeš; Primož Peterka;c\n')
    d.write('Kljub temu da je bil Leon Štukelj izjemen gimnastik, pa je tudi dokončal študij:; Fizike; Prava; Medicine;b')



    def izberi_temo(self):
        tema = input('Izberite temo, vnesite 1, 2 ali 3: \n 1) Nogomet \n 2) Košarka \n 3) Slovenski šport \n Tema: ')
        while tema not in '123':
            tema = input('Temo lahko izberete le tako, da vnesete 1, 2 ali 3: ')
        if tema == '1':
            self.izbor = 'Nogomet.txt'
        elif tema == '2':
            self.izbor = 'Kosarka.txt'
        elif tema == '3':
            self.izbor = 'Slo_sport.txt'



    def konec(self):
        print('Prišli ste do konca {}, pravilno ste odgovorili na {} vprašanj od treh.'.format(self.ime, self.pravilnih))
        znova = input('Če bi želeli igrati še enkrat (morda izbrati drugo temo) vtipkaje OK, sicer ste zaključili: ')
        if znova in ['OK', 'ok', 'Ok']:
            izvedi()


            
def izvedi():
    izberi_temo(kviz)
    seznam  = []
    datoteka = kviz.izbor
    with open(datoteka, 'r') as f:
        for vrstica in f:
            seznam.append(vrstica.strip().split(';'))
    for vpr in seznam:
        print(vpr[0])
        print('a)' + vpr[1])
        print('b)' + vpr[2])
        print('c)' + vpr[3])
        odg = input('Odgovor je: ')
        while odg not in 'abc':
            odg = input('Odgovorite lahko le tako, da vnesete a, b ali c! Odgovor je: ')
        preveri(vpr, odg)
    konec(kviz)



def preveri(sez, odg):
    pravilen_odgovor = sez[4]
    if odg == pravilen_odgovor:
        kviz.pravilnih += 1
        print('Odgovor je pravilen!')
    else:
        print('Odgovor ni pravilen, pravilen odgovor je {}.'.format(pravilen_odgovor) )

        


kviz = Kviz()
izvedi()



    
 



               
