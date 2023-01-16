"""
Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea.

Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l

"""

sukupuoli = input("Anna biologinen sukupuolesi: ")
hemoglobiini = float(input("Anna hemoglobiiniarvosi (g/l): "))

if sukupuoli=="Nainen":
    if hemoglobiini<117:
        print("Hemoglobiiniarvosi on alhainen. ")
    elif hemoglobiini>175:
        print("Hemoglobiiniarvosi on korkea. ")
    else:
        print("Hemoglobiiniarvosi on normaali. ")

if sukupuoli=="Mies":
    if hemoglobiini<134:
        print("Hemoglobiiniarvosi on alhainen. ")
    elif hemoglobiini>195:
        print("Hemoglobiiniarvosi on korkea. ")
    else:
        print("Hemoglobiiniarvosi on normaali")