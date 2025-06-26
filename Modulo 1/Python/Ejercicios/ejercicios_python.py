# # EJERCICIO 1

# nombre = "Manolo"
# edad = 20
# ciudad = "Miami"

# print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")

# # EJERCICIO 2

# estudiante = "Michael"
# nota1 = 20
# nota2 = 17
# nota3 = 10
# promedio = (nota1 + nota2 + nota3) / 3
# print(f"Estudiante: {estudiante}, Promedio de notas: {promedio}")

# # form = input("Cual es tu nombre: ")
# # formNum = int(input("Escribe un numero: "))

# # EJERCICIO 3
# num1 = int(input("Ingresa un numero: "))
# num2 = int(input("Ingresa otro numero: "))
# suma = num1 + num2
# resta = num1 - num2
# multiplicacion = num1 * num2
# division = num1 / num2
# print(f"Suma: {suma}, Resta: {resta}, Multiplicacion: {multiplicacion}, Division: {division}")

# # EJERCICIO 4
# evenNum = int(input("Escribe un numero: "))
# isEven = evenNum % 2
# modulo = isEven == 0
# print(f"Numero: {evenNum}, es par: {modulo}")

# # EJERCICIO 5
# num3 = int(input("Por favor ingrese un numero: "))
# mayorDiez = num3 > 10
# menorVeinte = 20 > num3
# print(f"Mayor que 10: {mayorDiez}, y menor que veinte: {menorVeinte}")

# EJERCICIO 6
calificacion = int(input("Escribe tu calificacion: "))

if calificacion >= 90: #or calificacion <= 100:
    print("Tienes un grado A")
elif calificacion >= 80: #or calificacion <= 89:
    print("Tienes un grado B")
elif calificacion >= 70: #or <= 79:
    print("Tienes un grado C")
elif calificacion >= 60: #or <= 69:
    print("Tienes un grado D")
elif calificacion >= 0: # or <= 59:
    print("Tienes una calificacion de F")
else:
    print("No tienes calificacion")