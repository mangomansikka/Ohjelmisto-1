"""
Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
Laskenta perustuu tietokannasta haettuihin koordinaatteihin.
Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
Kirjoita hakukenttään geopy ja vie asennus loppuun.

"""

import mysql.connector
from geopy import distance

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='cindy',
    password='5206xx',
    autocommit=True
    )

def etäisyys(koodi):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident='" + koodi + "'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

lentokenttä1 = input("Anna ensimmäisen lentokentän ICAO-koodi: ")
lentokenttä2 = input("Anna toisen lentokentän ICAO-koodi: ")
tulos1 = etäisyys(lentokenttä1)
tulos2 = etäisyys(lentokenttä2)
dist = distance.distance(tulos1, tulos2)
print(f"Etäisyys on {dist}")