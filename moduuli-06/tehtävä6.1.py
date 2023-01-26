"""
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen
nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan
kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

"""
import random

def satunnainen_silmäluku():
    silmäluku = random.randint(1, 6)
    print(silmäluku)
    return silmäluku
while satunnainen_silmäluku()!=6:
    satunnainen_silmäluku()
else:
    print("Toiminto lopetetttu. ")