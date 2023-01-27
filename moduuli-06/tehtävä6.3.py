"""
Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja
palauttaa paluuarvonaan vastaavan litramäärän. Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä
ja muuntaa sen litroiksi. Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
kunnes käyttäjä syöttää negatiivisen gallonamäärän.
Yksi gallona on 3,785 litraa.

"""
def muutos(gallonat):
    litra= gallonat * 3.785
    return litra

annettu_arvo = float(input("Anna bensiiinin määrä Yhdysvaltain nestegallonoina: "))
vastaus = muutos(annettu_arvo)

while muutos(annettu_arvo)>0:
    print(f"Nestegallonat litroina: {vastaus}")
    annettu_arvo = float(input("Anna bensiiinin määrä Yhdysvaltain nestegallonoina tai lopeta syöttämällä negatiivinen luku: "))
    vastaus = muutos(annettu_arvo)
else:
    print("Toiminto lopetettu. ")