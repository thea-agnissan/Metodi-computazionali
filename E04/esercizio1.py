import pandas as pd
import matplotlib.pyplot as plt



url = "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv"


df = pd.read_csv(url)


print(df.columns)


# PUNTO 3: Grafico del flusso in funzione del tempo 

plt.figure(figsize=(10, 5)) # Crea la prima finestra grafica
plt.plot(df['TIME'], df['PDCSAP_FLUX'])
plt.xlabel("Tempo (BJD - 2454833)")
plt.ylabel("Flusso (e-/s)")
plt.title("Curva di luce - Linea continua")

#PUNTO 4: Grafico del flusso con punti
plt.figure(figsize=(10, 5)) # Crea una seconda finestra grafica separata
plt.plot(df['TIME'], df['PDCSAP_FLUX'], 'o', markersize=2) # 'o' traccia i punti[cite: 3]
plt.xlabel("Tempo (BJD - 2454833)")
plt.ylabel("Flusso (e-/s)")
plt.title("Curva di luce - Solo punti")

"""
punto5: Produre un grafico del flusso in funzione del tempo utilizzando le barre d'errore 
(suggerimento: usare pyplot.errorbar). La colonna degli errori nel DataFrame è 
PDCSAP_FLUX_ERR
Salvare il risultato in un file immagine (formato png o pdf) usando plt.savefig()
"""

plt.figure(figsize=(10, 5))
plt.errorbar(
    df['TIME'], 
    df['PDCSAP_FLUX'], 
    yerr=df['PDCSAP_FLUX_ERR'], 
    fmt='o', 
    markersize=2, 
    ecolor='gray', 
    alpha=0.5
)
plt.xlabel("Tempo")
plt.ylabel("Flusso")
plt.title("Curva di luce con barre d'errore") 

#salvo il grafico in formato PNG
plt.savefig("curva_di_luce_errori.png", dpi=300)
print("Grafico con barre d'errore salvato con successo come 'curva_di_luce_errori.png'!")


#capisco dove sta il minimo
# Trova l'indice della riga in cui il flusso è al minimo
indice_minimo = df['PDCSAP_FLUX'].idxmin()

# Leggi il valore del tempo in corrispondenza di quell'indice
tempo_del_minimo = df.loc[indice_minimo, 'TIME']
print("Il minimo si trova al tempo:", tempo_del_minimo)

# PUNTO 6: Zoom su un intervallo temporale attorno a un minimo
# Selezioniamo un intervallo temporale attorno al minimo del transito
# Nota: puoi aggiustare i valori di tempo in base a dove si trova il minimo nel tuo grafico generale
t_min = 131.5
t_max = 134.5

# Utilizziamo .loc per filtrare il DataFrame nell'intervallo scelto
"""
.loc è lo strumento principale che si usa per selezionare e filtrare righe e
 colonne di un DataFrame in base a determinate condizioni logiche.
Nel nostro caso prendo dal DataFrame originale df solo quelle righe in cui il valore della colonna TIME è maggiore o uguale a 
t_min e contemporaneamente (&) minore o uguale a t_max".
In questo modo viene creato un nuovo DataFrame più piccolo (df_zoom) che contiene solo i dati relativi a quel determinato intervallo di tempo.
"""
df_intervallo = df.loc[(df['TIME'] >= t_min) & (df['TIME'] <= t_max)]

plt.figure(figsize=(10, 5))
plt.errorbar(
    df_intervallo['TIME'], 
    df_intervallo['PDCSAP_FLUX'], 
    yerr=df_intervallo['PDCSAP_FLUX_ERR'], 
    fmt='o', 
    markersize=3, 
    ecolor='gray', 
    alpha=0.6
)
plt.xlabel("Tempo")
plt.ylabel("Flusso")
plt.title("Intervallo temporale attorno a un minimo")



#Mostra i grafici
plt.show()
