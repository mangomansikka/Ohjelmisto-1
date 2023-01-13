import math

leiviskät_str = input("Anna leiviskät: ")
naulat_str = input("Anna naulat: ")
luodit_str = input("Anna luodit: ")

luodit = 13.3
naulat = 32*luodit
leiviskät = 20*naulat

leiviskät_ = float(leiviskät_str)
naulat_ = float(naulat_str)
luodit_ = float(luodit_str)

massa_grammoina = (leiviskät*leiviskät_)+(naulat*naulat_)+(luodit*luodit_)
massa_kilogrammoina = math.floor(massa_grammoina/1000)

print(f"Massa nykymittojen mukaan: ")
print(str(massa_kilogrammoina) + " kilogrammaa ja " + str(round(massa_grammoina-massa_kilogrammoina*1000, 2)) + " grammaa. ")