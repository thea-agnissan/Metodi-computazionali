import math

#ESERCIZIO 0
def somma_naturali(n):
    """Restituisce la somma dei primi n numeri naturali"""
    somma = 0
    for i in range(1, n + 1):
        somma += i
    return somma

def somma_radici(n):
    """Restituisce la somma delle radici quadrate dei primi n numeri naturali """
    somma = 0.0
    for i in range(1, n + 1):
        somma += math.sqrt(i)
    return somma

#ESERCIZIO 1
def somma_e_prodotto(n):
    """Restituisce la somma e il prodotto dei primi n numeri naturali"""
    somma = 0
    prodotto = 1
    
    for i in range(1, n + 1):
        somma += i
        prodotto *= i
        
    return somma, prodotto

def somma_potenze(n, alpha=1):
    """Restituisce la somma di i^alpha da i=0 a n """
    somma = 0
    for i in range(0, n + 1):
        somma += i ** alpha
    return somma