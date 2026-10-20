#Somma dei primi N numeri naturali
N = int(input("Inserisci un numero naturale: "))
print("Il numero inserito è: ", N )
somma = 0
for i in range(N + 1):
   somma = somma + i
print("La somma dei primi", N, "numeri naturali è ", somma)
