"""
Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka, kunnes käyttäjä syöttää tyhjän merkkijonon.
Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan,
syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain
mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

"""
import random

def sama(nimi, lista):
    arvo = 1
    for n in lista:
        if n == nimi:
            arvo = 0
    return arvo

syöttö = input("Anna nimi: ")
nimilista = set()

while True:
    if syöttö!="":
        vastaus = sama(syöttö, nimilista,)
        if vastaus==1:
            nimilista.add(syöttö)
            syöttö = input("Uusi nimi. Anna nimi tai lopeta painamalla enter: ")
        else:
            syöttö = input("Aiemmin syötetty. Anna toinen nimi tai lopeta painamalla enter: ")
    else:
        break

lopullinen_lista = list(nimilista)
random.shuffle(lopullinen_lista)
for x in lopullinen_lista:
    print(x)
