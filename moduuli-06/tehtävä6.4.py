"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma,
jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

"""
def lista(summa):
    return sum(summa)
lista1=[]
kokonaisluku = int(input("Anna kokonaisluku: "))

while True:
    lista1.append(kokonaisluku)
    kokonaisluku = input("Anna kokonaisluku tai lopeta syöttämällä enter: ")
    if kokonaisluku!="":
        kokonaisluku = int(kokonaisluku)
    else:
        break
vastaus = lista(lista1)

print(f"Annettujen lukujen summa: ", vastaus)
