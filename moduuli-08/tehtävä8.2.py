"""
Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI) ja tulostaa kyseisessä maassa olevien lentokenttien
lukumäärät tyypeittäin. Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

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

def hae_lentokenttä(maakoodi):
    sql = "SELECT type, count(*) FROM airport WHERE iso_country= '" + maakoodi + "' GROUP BY type"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

koodi = input("Anna maakoodi: ")
tulos = hae_lentokenttä(koodi)
print(tulos)