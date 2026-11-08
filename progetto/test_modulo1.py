import numpy as np
from modulo1 import pianeta #serve a importare la classe che hai scritto nel modulo all'interno dello script di test

# Creo un array con alcuni pianeti del sistema solare inserendo i dati reali
# Usiamo dtype=object per permettere a NumPy di gestire array di istanze di classi
array_pianeti = np.array([
    pianeta("Terra", massa=6*10**24, raggio=6378, distanza_sole=1),
    pianeta("Giove", massa=1.9*10**27, raggio=71492, distanza_sole=5.203),
    pianeta("Mercurio", massa=3.33*10**23, raggio=2439.7, distanza_sole=0.387),
    pianeta("Urano", massa=8.7*10**25, raggio=25559, distanza_sole=19.191)
], dtype=object)

#printo prima l'array non ordinato
print("--- Array prima del sort ---")
for p in array_pianeti:
    print(p)

# Ordinamento dell'array tramite la funzione sort di numpy
# NumPy sfrutterà automaticamente i metodi __lt__ e __gt__ definiti nella classe
array_ordinato = np.sort(array_pianeti)

print("\n--- Array dopo il sort (ordinato per distanza dal Sole) ---")
for p in array_ordinato:
    print(p)