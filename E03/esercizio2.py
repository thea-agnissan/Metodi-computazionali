"""
Esercizio 2
Creare uno script python che:

chieda in input un valore intero e il numero di bit cui applicare delle operazioni di bit shift;
stampi il valore intero in rappresentazione binaria ed esadecimale;
satmpi il risultato delle operazioni di bit shift (<< e>>) sia in rappresentazione binaria che esadecimale.
"""
valore = int(input("Inserisci un numero intero: "))
num_bit = int(input("Inserisci il numero di bit per il shift: "))

#Stampa del valore originale in binario ed esadecimale
print("Il valore del numero inserito è:")
print(f"Decimale:    {valore}")
print(f"Binario:     {bin(valore)}")
print(f"Esadecimale: {hex(valore)}")


shift_left = valore << num_bit
shift_right = valore >> num_bit

# Stampa del risultato dello Shift a Sinistra (<<)
print(f"Shift a Sinistra ({valore} << {num_bit})")
print(f"Decimale:    {shift_left}")
print(f"Binario:     {bin(shift_left)}")
print(f"Esadecimale: {hex(shift_left)}")

# Stampa del risultato dello Shift a Destra (>>)
print(f"Shift a Destra ({valore} >> {num_bit})")
print(f"Decimale:    {shift_right}")
print(f"Binario:     {bin(shift_right)}")
print(f"Esadecimale: {hex(shift_right)}")
