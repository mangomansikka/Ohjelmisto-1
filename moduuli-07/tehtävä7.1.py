"""
Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan
(kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi

"""
vuodenajat = ("talvi", "talvi", "kevät", "kevät", "kevät" , "kesä", "kesä", "kesä" , "syksy", "syksy", "syksy" , "talvi")
järjestysnumero = int(input("Anna kuukauden järjestysnumero (1-12): "))
kuukaudet = vuodenajat[järjestysnumero-1]
print(f"{järjestysnumero}. kuukauden vastaava vuodenaika on {kuukaudet}. ")