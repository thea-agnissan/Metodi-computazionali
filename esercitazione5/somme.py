"""Restituisce la somma delle radici quadrate dei primi n numeri naturali (da 1 a n)."""
def somma_radici(n):
    somma = 0.0
    for i in range(1, n + 1):
        somma += math.sqrt(i)
    return somma

#SECONDA PARTE: esercizio 1
"""Restituisce la somma e il prodotto dei primi n numeri naturali."""
def somma_e_prodotto(n):
   
    somma = sum(range(1, n + 1))
    prodotto = 1
    for i in range(1, n + 1):
        prodotto *= i
    return somma, prodotto

"""Restituisce la somma di i^alpha da i=0 a n (alpha ha valore di default pari a 1)."""
def somma_potenze(n, alpha=1):
    somma = 0.0
    for i in range(0, n + 1):
        somma += i ** alpha
    return somma