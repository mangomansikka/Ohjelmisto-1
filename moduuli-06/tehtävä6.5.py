"""
Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin parametrina saatu lista
paitsi että siitä on karsittu pois kaikki parittomat luvut. Kirjoita testausta varten pääohjelma,
jossa luot listan, kutsut funktiota ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

"""

lista1=[]
kokonaisluku= int(input("Anna kokonaisluku: "))

while True:
    lista1.append(kokonaisluku)
    kokonaisluku = input("Anna kokonaisluku tai lopeta syöttämällä enter: ")
    if kokonaisluku!="":
        kokonaisluku = int(kokonaisluku)
    else:
        break
def lista(lista1):
    for n in lista1:
        if n % 2!=0:
            lista1.remove(n)
    return
print(f"Alkuperäinen lista: ", lista1)
lista(lista1)
print(f"Karsittu lista, jossa on vain parilliset kokonaisluvut: ", lista1)