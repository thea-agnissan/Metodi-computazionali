import somme

n = 5
alpha = 1

# 1. Somma dei primi n numeri naturali
risultato_somma = somme.somma_naturali(n)
print(f"La somma dei primi {n} numeri naturali è: {risultato_somma}")

# 2. Somma delle radici dei primi n numeri naturali
risultato_radici = somme.somma_radici(n)
print(f"La somma delle radici dei primi {n} numeri naturali è: {risultato_radici:.4f}")

# 3. Test della somma e del prodotto dei primi n numeri naturali
s, p = somme.somma_e_prodotto(n)
print(f"La somma dei primi {n} numeri naturali è: {s}")
print(f"Il prodotto dei primi {n} numeri naturali è: {p}")

# 4. Test della somma delle potenze i^alpha da 0 a n (con alpha specificato)
risultato_potenze = somme.somma_potenze(n, alpha)
print(f"La somma di i^{alpha} (da 0 a {n}) è: {risultato_potenze}")
