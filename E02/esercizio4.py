#Calcola la tua età
from datetime import datetime, timedelta
data_di_nascita = input("Inserisci la tua data di nascita giorno-mese-anno")

# Converto la stringa inserita 
data_nascita = datetime.strptime(data_di_nascita, "%d-%m-%y")

data_attuale = datetime.now()

# Calcolo l'età in anni, giorni e secondi
# Calcolo degli anni 
eta_anni = data_attuale.year - data_nascita.year

# Calcolo della differenza esatta come timedelta
differenza = data_corrente - data_nascita

eta_giorni = differenza.days
eta_secondi = int(differenza.total_seconds())

print("\n--- LA TUA ETÀ ---")
print(f"{'Anni:':<12} {eta_anni:>10}")
print(f"{'Giorni:':<12} {eta_giorni:>10,}".replace(",", "."))  # Usa il punto come separatore delle migliaia
print(f"{'Secondi:':<12} {eta_secondi:>10,}".replace(",", ".")) 
