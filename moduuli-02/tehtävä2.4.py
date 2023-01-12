import math

ensimmäinen_kokonaisluku_str = input("Anna ensimmäinen kokonaisluku: ")
toinen_kokonaisluku_str = input("Anna toinen kokonaisluku: ")
kolmas_kokonaisluku_str = input("Anna kolmas kokonaisluku: ")

ensimmäinen_kokonaisluku = float(ensimmäinen_kokonaisluku_str)
toinen_kokonaisluku = float(toinen_kokonaisluku_str)
kolmas_kokonaisluku = float(kolmas_kokonaisluku_str)


summa = ensimmäinen_kokonaisluku + toinen_kokonaisluku + kolmas_kokonaisluku
tulo = ensimmäinen_kokonaisluku * toinen_kokonaisluku * kolmas_kokonaisluku
keskiarvo = (ensimmäinen_kokonaisluku + toinen_kokonaisluku + kolmas_kokonaisluku)/3

print(f"Summa on " + str(summa))
print(f"Tulo on " + str(tulo))
print(f"Keskiarvo on " + str(keskiarvo))