"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan
nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

"""
import random

maksimi = int(input("Anna nopan maksimisilmäluku: "))
vastaus = 0
def satunnainen_silmäluku(maksimi):
        return random.randint(1, maksimi)

while vastaus!=maksimi:
    vastaus = satunnainen_silmäluku(maksimi)
    print(vastaus)
else:
    print("Toiminto lopetettu. ")
