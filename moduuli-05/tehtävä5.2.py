"""
Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True.

"""

lista = []
luku = input("Anna luku: ")

while luku!="":
    lista.append(int(luku))
    luku = input("Anna luku: ")

if luku=="":
    if lista==[]:
        print("Ei ole numeroita, joita voisi listata. Toiminto lopetettu. ")
    else:
        print(sorted(lista, reverse=True))
        print("Toiminto lopetettu. ")