"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan
nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

"""
import random

def satunnainen_silmäluku(raja):
        return random.randint(1, raja)

maksimi = int(input("Anna nopan maksimisilmäluku: "))
vastaus = satunnainen_silmäluku(maksimi)

while vastaus!=maksimi:
    vastaus = satunnainen_silmäluku(maksimi)
    print(vastaus)
else:
    print("Toiminto lopetettu. ")
