"""
Kirjoita ohjelma, joka kysyy käyttäjältä laivan hyttiluokan (LUX, A, B, C) ja
tulostaa sen sanallisen kuvauksen alla olevan luettelon mukaisesti.
Tehtävässä on käytettävä if/elif/else-toistorakennetta.

LUX on parvekkeellinen hytti yläkannella.
A on ikkunallinen hytti autokannen yläpuolella.
B on ikkunaton hytti autokannen yläpuolella.
C on ikkunaton hytti autokannen alapuolella.
Jos käyttäjä syöttää kelvottoman hyttiluokan, ohjelma tulostaa Virheellinen hyttiluokka.

"""

hyttiluokka = input("Anna laivan hyttiluokka: ")

if hyttiluokka=="LUX":
    print("Hyttiluokka on parvekkeellinen hytti yläkannella")

elif hyttiluokka=="a" or "b":
    print("Hyttiluokka on ikkunaton hytti autokannen yläpuolella. ")

else:
    print("Hyttiluokka on ikkunaton hytti autokannen alapuolella. ")