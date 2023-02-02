"""
Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

"""
import math
def pinta_ala(halkaisija, hinta):
    a = (halkaisija**2*math.pi/4)/1000
    hinta_e = hinta/a
    return hinta_e

halk1 = int(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
halk2 = int(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta1 = int(input("Anna ensimmäisen pizzan hinta euroina: "))
hinta2 = int(input("Anna toisen pizzan hinta euroina: "))

yksikköhinta1 = pinta_ala(halk1, hinta1)
yksikköhinta2 = pinta_ala(halk2, hinta2)
#print(yksikköhinta1)
#print(yksikköhinta2)
if yksikköhinta2>yksikköhinta1:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle. ")
else:
    print("Toinen pizza antaa paremman vastineen rahalle. ")
