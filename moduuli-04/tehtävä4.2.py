"""
Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi
niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

"""

tuumat = float(input("Anna tuumat: "))

while tuumat>0:
    senttimetrit = 2.54 * tuumat
    print(f"Tuumat senttimetreinä: " + str(senttimetrit))
    tuumat = float(input("Anna tuumat: "))

else:
    print("Toiminto lopetettu. ")