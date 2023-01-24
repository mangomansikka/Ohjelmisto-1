"""
Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.


"""

vastaus = True
while True:
    kokonaisluku = int(input("Anna kokonaisluku: "))
    raja = kokonaisluku-1

    for n in range(2, raja):
        if kokonaisluku % n==0:
            vastaus = False
    if vastaus==False:
        print("Luku ei ole alkuluku. ")
        break
    else:
        print("Luku on alkuluku. ")
        break
