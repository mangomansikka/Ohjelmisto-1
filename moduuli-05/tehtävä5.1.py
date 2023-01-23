"""
Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
Käytä for-toistorakennetta.

"""
import random

lista = []
arpakuutio = int(input("Anna arpakuutioiden lukumäärä: "))
heitto = 0
kaikki = 0
print("Arpakuutioiden silmäluvut: ")

while arpakuutio>heitto:
    satunnainen = random.randint(1, 6)
    lista.append(int(satunnainen))
    heitto = heitto + 1

else:
    for n in lista:
        print(n)
    for n in range(0, len(lista)):
        kaikki = kaikki + lista[n]
    print("Silmälukujen summa on ", kaikki)