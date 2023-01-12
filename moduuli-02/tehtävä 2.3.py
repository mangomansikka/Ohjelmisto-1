

suorakulmion_kanta_str = input("Anna suorakulmion kanta metreinä: ")
suorakulmion_korkeus_str = input ("Anna suorakulmion korkeus metreinä: ")

suorakulmion_kanta = float(suorakulmion_kanta_str)
suorakulmion_korkeus = float(suorakulmion_korkeus_str)

suorakulmion_piiri = suorakulmion_korkeus + suorakulmion_kanta + suorakulmion_korkeus + suorakulmion_kanta
print(f"Suorakulmion piiri on: " + str(suorakulmion_piiri))

suorakulmion_pinta_ala = suorakulmion_korkeus*suorakulmion_kanta
print(f"Suorakulmion pinta-ala on: " + str(suorakulmion_pinta_ala))