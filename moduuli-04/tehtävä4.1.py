"""
Kirjoita while-toistorakennetta käyttävä ohjelma,
joka tulostaa kolmella jaolliset luvut väliltä 1..1000
"""

numero = 0
while numero<1000:
    while numero % 3==0:
        print(numero)
        numero = numero + 1
    else:
        numero = numero + 1
