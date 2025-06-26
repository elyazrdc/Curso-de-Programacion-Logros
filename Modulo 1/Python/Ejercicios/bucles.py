# Bucle For
for x in range (1, 6):
    print(f"Los numeros del uno al cinco: {x}")

for x in "Hola":
    print(x)

# Bucle While
import math
numero = int(input("Digite un numero: "))

while numero < 0:
    print("Error. Debe ser un numero positivo")
    numero = int(input("Digite un numero: "))
print(numero)