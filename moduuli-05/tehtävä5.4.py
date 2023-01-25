"""
Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan
(käytä for-toistorakennetta nimien kysymiseen) ja tallentaa ne listarakenteeseen.
Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä
kuin ne syötettiin. Käytä for-toistorakennetta nimien kysymiseen
ja for/in toistorakennetta niiden läpikäymiseen.

"""

toisto = 0
lista1=[]

while toisto<5:
    toisto = toisto + 1
    lista1.append(toisto)

if toisto>=5:
    lista2 = []
    for n in lista1:
        kaupunki = input("Anna kaupungin nimi: ")
        lista2.append(kaupunki)
    for x in lista2:
        print(x)