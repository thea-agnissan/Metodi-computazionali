import numpy as np
import matplotlib.pyplot as plt

# Numero di campioni da generare
N = 1000

# METODO 1: METODO DELLA CUMULATIVA

z = np.random.uniform(0, 1, N) #funzione di numpy che genera numeri casuali uniformemente distribuiti tra 0 e 1

# 2. Applichiamo la formula della funzione inversa ricavata analiticamente:
# x = (1000 * z)**(1/3)
x_cumulativa = (1000 * z) ** (1 / 3)


# METODO 2: HIT OR MISS
#definiamo la funzione di densità di probabilità della distribuzione 
def p(x):
    return (3/1000) * x**2

"""
analiticamente trovo il valore massimo che può assumere la funzione di densità di 
probabilità p(x) nell'intervallo [0, 10]. Sapendo che p(x) è una funzione crescente,
il massimo si trova in x=10: p(10) = (3/1000) * 10**2 = 0.3
"""
y_max = 0.3

x_hit_miss = []
#Creo un ciclo che continua a ripetere il tiro al bersaglio finché non a raccoglie esattamente N valori validi
while len(x_hit_miss) < N:
  # Generiamo un punto casuale (x, y) nel rettangolo [0, 10] x [0, 0.3]
  x_rand = np.random.uniform(0, 10)
  y_rand = np.random.uniform(0, y_max)

  # Se y_rand si trova "sotto" la curva p(x), accettiamo il valore di x
  if y_rand <= p(x_rand):
    x_hit_miss.append(x_rand) #salvo x nella lista

# Convertiamo la lista in un array numpy
x_hit_miss = np.array(x_hit_miss)

#GRAFICI
plt.figure(figsize=(10, 5))


# Istogramma della cumulativa (in blu trasparente)
"""
E' una funzione di matplotlib che prende in input un insieme di dati numerici, li suddivide in intervalli 
e conta quanti valori cadono all'interno di ciascun intervallo, tracciando le barre corrispondenti.
"""
plt.hist(
    x_cumulativa,
    bins=30,
    density=True,
    alpha=0.5,
    label="Metodo Cumulativa",
    color="blue",
)

# Istogramma del metodo hit or miss (in arancione trasparente)
plt.hist(
    x_hit_miss,
    bins=50,
    density=True,
    alpha=0.5,
    label="Metodo Hit or Miss",
    color="orange",
)

plt.title(
    "Confronto tra Metodo della Cumulativa e Hit or Miss", fontsize=12
)
plt.xlabel("x")
plt.ylabel("Densità di probabilità")
plt.legend()
plt.grid(True)
plt.show()