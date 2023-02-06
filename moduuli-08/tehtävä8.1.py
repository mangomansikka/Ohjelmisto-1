"""
Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen ja sen sijaintikunnan kurssilla käytettävästä
lentokenttätietokannasta. ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

"""

import mysql.connector

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='cindy',
    password='5206xx',
    autocommit=True
    )

def hae_lentokenttä(icao):
    sql = "SELECT name, municipality FROM airport WHERE ident='" + icao + "'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result

lentokenttä = input("Anna lentokentän ICA0-koodi: ")
tulos = hae_lentokenttä(lentokenttä)
print(tulos)
