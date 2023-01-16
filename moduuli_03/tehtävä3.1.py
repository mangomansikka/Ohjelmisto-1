"""
Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
Kuha on alamittainen, jos sen pituus on alle 37 cm.

"""
import math
kuhan_pituus = float(input("Anna kuhan pituus senttimetreinä: "))
vajaa_pituus = 37-kuhan_pituus

if kuhan_pituus<37:
    print(f"Kuha on alamittainen.  Mitta on pyyntimitasta vajaa " + str(vajaa_pituus) + "cm. Laske kuha takaisin järveen. ")

else:
    print(f"Kuha on pyyntimitan mukainen. Voit ottaa kuhan. ")