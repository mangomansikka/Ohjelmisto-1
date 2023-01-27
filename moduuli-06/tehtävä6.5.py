"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista
paitsi että siitä on karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma,
jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

"""
def lista(karsinta):
    for n in karsinta:
        if n % 2!=0:
            karsinta.remove(n)
    return karsinta
lista1=[]
kokonaisluku= int(input("Anna kokonaisluku: "))

while True:
    lista1.append(kokonaisluku)
    kokonaisluku = input("Anna kokonaisluku tai lopeta syöttämällä enter: ")
    if kokonaisluku!="":
        kokonaisluku = int(kokonaisluku)
    else:
        break
print(f"Alkuperäinen lista: ", lista1)
vastaus = lista(lista1)
print(f"Karsittu lista, jossa on vain parilliset kokonaisluvut: ", vastaus)