"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja
palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä
ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.

"""
bensiini = int(input("Anna bensiiinin määrä Yhdysvaltain nestegallonoina: "))
def muutos():
    litramäärä = bensiini*3.785
    return litramäärä

while bensiini>0:
    print(f"Nestegallonat litroina: {muutos()}")
    bensiini = int(input("Anna bensiiinin määrä Yhdysvaltain nestegallonoina tai lopeta syöttämällä negatiivinen luku: "))
else:
    print("Toiminto lopetettu. ")