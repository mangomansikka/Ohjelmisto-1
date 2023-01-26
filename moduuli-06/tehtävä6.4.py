"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa listassa olevien lukujen summan. Kirjoita testausta varten pääohjelma,
jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

"""
lista1=[]
kokonaisluku= int(input("Anna kokonaisluku: "))
def lista():
    return sum(lista1)

while True:
    lista1.append(kokonaisluku)
    kokonaisluku = input("Anna kokonaisluku tai lopeta syöttämällä enter: ")
    if kokonaisluku!="":
        kokonaisluku = int(kokonaisluku)
    else:
        break
print(f"Annettujen lukujen summa: ", lista())
