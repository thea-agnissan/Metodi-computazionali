#liste
giorni_settimana = ['lunedì','martedì','mercoledì','giovedì','venerdì','sabato','domenica']

aggiungo_giorno = []
dizionario_ottobre = {}
indice = 3
for giorno in range(1,32):
    nome_giorno = giorni_settimana[indice]
    aggiungo_giorno.append(nome_giorno)

    dizionario_ottobre[giorno] = nome_giorno
    indice = (indice + 1) % 7

print("Correlazione giorni ottobre 2026")
for giorno_mese, giorno_settimana in dizionario_ottobre.items():
    print(f"Il {giorno_mese} ottobre 2025 è {giorno_settimana}")
