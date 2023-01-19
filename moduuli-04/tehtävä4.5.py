"""
Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
(Oikea käyttäjätunnus on python ja salasana rules).

"""

oikea_käyt = str("python")
oikea_sal = str("rules")
syöttö = 0


while True:
    käyttäjätunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    syöttö += 1
    if käyttäjätunnus!=oikea_käyt or salasana !=oikea_sal:
        print("Käyttäjätunnus tai salasana on väärin. ")

    elif käyttäjätunnus==oikea_käyt and salasana==oikea_sal:
        print("Tervetuloa. ")
        break
    if (käyttäjätunnus!=oikea_käyt or salasana!=oikea_sal) and syöttö>=5:
        print("Pääsy evätty. ")
        break