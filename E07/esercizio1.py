import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simpson

"""
Si è ricavata analiticamente la formula per il periodo di oscillazione in funzione del punto 
di partenza x0 con una funzione energia potenziale V(x) = kx^6
"""

# Parametri fisici del sistema
k = 0.1   # Costante del potenziale
m = 1.0   # Massa

# Valori del punto di partenza x0 per cui calcolare il periodo T
x0_values = np.linspace(0.2, 5.0, 50)

# Definizione della funzione di energia potenziale V(x)
def V(x):
    return k * (x ** 6)

# 1. Funzione per calcolare il periodo T dato un punto di partenza x0
def calcola_periodo(x0, m, V, num_punti=1000):
    if x0 == 0:
        return 0.0
    
    # Creiamo un array di punti tra 0 e x0
    # Evito x0 per non avere zero a denominatore dell'integranda 
    x = np.linspace(0, x0 * 0.9999, num_punti)
    
    # Calcoliamo il denominatore: sqrt(V(x0) - V(x))
    denominatore = np.sqrt(V(x0) - V(x))
    
    # Funzione integranda: 1 / sqrt(V(x0) - V(x))
    integranda = 1.0 / denominatore
    
    """
    Integrazione numerica con il metodo di Simpson; gli passiamo i due array e lui calcola
    l'area sotto la curva del primo array rispetto alle coordinate del secondo
    """
    integrale = simpson(integranda, x)
    
    # Moltipliciamo per sqrt(8m) come da formula teorica
    T = np.sqrt(8 * m) * integrale
    return T


# 3. Potenziale armonico V(x) = k * x^2
"""
Dobbiamo rifare lo stesso calcolo del periodo T e il grafico, 
ma cambiando la funzione di energia potenziale in un potenziale da oscillatore armonico
"""
def V_armonico(x):
    return k * (x ** 2)



# 4. Formula alternativa per il potenziale (semore rispettando la simmetria)
"""
Si testa un'ulteriore formula per il potenziale che sia sempre simmetrica rispetto all'origine.
Ho scelto V(x) = k * x^4.
"""

def V_x4(x):
    return k * (x ** 4)


T_x6 = [calcola_periodo(x0, m, V) for x0 in x0_values]
T_armonico = [calcola_periodo(x0, m, V_armonico) for x0 in x0_values]
T_x4 = [calcola_periodo(x0, m, V_x4) for x0 in x0_values]


#GRAFICI

plt.figure(figsize=(9, 6))

# Punto 2: grafico di T in funzione di x0 per V(x) = kx^6
plt.plot(x0_values, T_x6, label="$V(x) = kx^6$", color="pink", linewidth=2.2)

# Punto 3: confronto con il potenziale armonico V(x) = kx^2
plt.plot(x0_values, T_armonico, label="$V(x) = kx^2$", color="purple", linewidth=2.2)

# Punto 4: confronto con V(x) = kx^4
plt.plot(x0_values, T_x4, label="$V(x) = kx^4$", color="blue", linewidth=2.2)

plt.title("Periodo $T$ in funzione della posizione iniziale $x_0$", fontsize=13)
plt.xlabel("Posizione iniziale $x_0$", fontsize=11)
plt.ylabel("Periodo $T$", fontsize=11)
plt.legend(fontsize=10)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()