import math

säde_str = input("Anna ympyrän säde metreinä: ")
säde = float(säde_str)
pinta_ala = math.pi*(säde*säde)
print(f"Ympyrän pinta-ala on: " + str(pinta_ala))