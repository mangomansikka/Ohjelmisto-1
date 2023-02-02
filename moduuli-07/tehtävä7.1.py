"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
(kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi

"""
"""
oma laiska kokeilu: 
vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät" , "kesä", "kesä", "kesä" , "syksy", "syksy", "syksy" , "talvi")
järjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12): "))
kuukaudet = vuodenajat[järjestysnumero-1]
print(f"{järjestysnumero}. kuukauden vastaava vuodenaika on {kuukaudet}. ")

"""

vuodenajat = ("kevät", "kesä", "syksy", "talvi")
kuukausi = int(input("Anna kuukauden numero (1-12): "))
kuukaudet = vuodenajat

if (kuukausi == 1 or kuukausi == 2):
    vuodenaika = vuodenajat[3]
elif (kuukausi >= 3 and kuukausi <= 5):
    vuodenaika = vuodenajat[0]
elif (kuukausi >=6 and kuukausi <=8):
    vuodenaika = vuodenajat[1]
elif(kuukausi >=9 and kuukausi<=11):
    vuodenaika = vuodenajat[2]
elif(kuukausi==12):
    vuodenaika = vuodenajat[3]
else:
    vuodenaika = "Nyt en kyllä osaa sanoa"
print(f"{kuukausi}. kuukauden vastaava vuodenaika on {vuodenaika}")