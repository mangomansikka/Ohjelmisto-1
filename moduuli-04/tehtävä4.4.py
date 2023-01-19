"""
Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.

"""
import random

kokonaisluku = int(input("Anna kokonaisluku väliltä 1-10: "))
random_kokonaisluku = random.randint(1, 10)

while kokonaisluku!=random_kokonaisluku:
    if kokonaisluku>random_kokonaisluku:
        kokonaisluku = int(input("Liian suuri arvaus. Anna kokonaisluku väliltä 1-10: "))

    else:
        kokonaisluku = int(input("Liian pieni arvaus. Anna kokonaisluku väliltä 1-10: "))

else:
    print("Oikein. ")