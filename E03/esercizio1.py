"""
Esercizio 1:
Creare uno script python che:

chieda in input 2 valori interi;
stampi i valori in rappresentazione binaria ed esadecimale;
satmpi il risultato delle operazioni AND e OR bitwise sia in rappresentazione binaria che esadecimale.
"""

a = int(input("Inserisci un numero intero "))
b = int(input("Inserisci un altro numero intero ")) #con int davanti a input sto convertendo la string in numero intero


print("Il valore del primo numero (", a, ") è :")
print("Binario:", bin(a))
print("Esadecimale:", hex(a))

print("Il valore del secondo numero (" ,b, ") è :")
print(" Binario:", bin(b))
print(" Esadecimale:", hex(b))

# risultato delle operazioni AND e OR bitwise in binario ed esadecimale
risultato_and = a & b
risultato_or = a | b


print("Operazione AND")

print(" Binario:",      bin(risultato_and))
print(" Esadecimale:" , hex(risultato_and))

print("Operazione OR")

print(" Binario:  ", bin(risultato_or))
print(" Esadecimale:", hex(risultato_or))

