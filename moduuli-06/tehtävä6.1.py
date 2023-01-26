"""
Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen
nopan silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan
kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

"""
import random

def satunnainen_silmäluku():
    return random.randint(1, 6)

vastaus = 0
while vastaus!=6:
    vastaus = satunnainen_silmäluku()
    print(vastaus)
