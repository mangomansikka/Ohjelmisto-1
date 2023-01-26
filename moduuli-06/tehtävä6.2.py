"""
Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan
nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

"""
import random

maksimi = int(input("Anna nopan maksimisilmäluku: "))
def satunnainen_silmäluku():
    return random.randint(1, maksimi)

heitot = 0
vastaus = 0
while vastaus!=maksimi:
    vastaus = satunnainen_silmäluku()
    heitot = heitot + 1
    print(vastaus)
else:
    tahkojen_summa = maksimi * heitot
    print(f"Tahkojen summa on {tahkojen_summa}. ")
