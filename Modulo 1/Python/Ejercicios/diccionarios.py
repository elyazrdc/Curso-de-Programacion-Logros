mi_diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

for x in mi_diccionario:
    print(x)

#Imprimir valor de un diccionario
print("Nombre: ", mi_diccionario["nombre"])
#Cambiar el valor de un diccionario
mi_diccionario["edad"] = 31

print("Edad: ", mi_diccionario["edad"])

#Añadir un nuevo clave-valor al diccionario
mi_diccionario["profesion"] = "Ingeniero"
print("Profesion: ", mi_diccionario["profesion"])

#Eliminar una clave-valor de un diccionario
del mi_diccionario["ciudad"]
print(mi_diccionario)

#Imprimir la longitud del diccionario
print("Longitud del diccionario: ", len(mi_diccionario))

#Comprobar si una clave esta en el diccionario
print("La clave nombre esta en el diccionario?", "nombre" in mi_diccionario)

# Iterar sobre una clave con bucle for
for clave in mi_diccionario:
    print(f"Clave: {clave}, Valor: {mi_diccionario[clave]}")


# EJERCICIO DE DICCIONARIO DE AULA
diccionario_aula = {
    "Elias Rivas": 18,
    "Arianyelina Rincon": 15,
    "Brian Mendez" : 10,
    "Carlos Villero": 18,
    "Damian Garcia": 13,
    "Decel Fernandez": 13,
    "Fabian Cardenas": 17,
    "Franklin Vecino": 16,
    "Helyanni Rodriguez": 16,
    "Liliana Rincon": 14,
    "Maria Macias": 16,
    "Over Machado": 16,
    "Paul Moran": 14,
    "Ronald Trujillo": 12,
    "Yuliexy Dimas": 10
}

print("\nDiccionario de la clase y sus notas:")
print("\n")
for clave in diccionario_aula:
    print(f"Nombre: {clave}, Nota: {diccionario_aula[clave]}")
#print(diccionario_aula)


#for x in diccionario_aula:
diccionario_aula["Arianyelina Rincon"] = 21
diccionario_aula["Franklin Vecino"] = 20
diccionario_aula["Carlos Villero"] = 21
diccionario_aula["Damian Garcia"] = 20
diccionario_aula["Elias Rivas"] = 20
diccionario_aula["Helyanni Rodriguez"] = 21
diccionario_aula["Liliana Rincon"] = 20
diccionario_aula["Maria Macias"] = 24
diccionario_aula["Yuliexy Dimas"] = 20
diccionario_aula["Paul Moran"] = 20
diccionario_aula["Over Machado"] = 20
diccionario_aula["Brian Mendez"] = 18
diccionario_aula["Fabian Cardenas"] = 21
diccionario_aula["Decel Fernandez"] = 17
diccionario_aula["Ronald Trujillo"] = 21

print("\nDiccionario de la clase y sus edades:")
print("\n")
for clave in diccionario_aula:
    print(f"Nombre: {clave}, Edad: {diccionario_aula[clave]}")

print("\nLa clave nombre esta en el diccionario?", "Elias Rivas" in diccionario_aula)

for valor in diccionario_aula.values():
    print("\nEdad: ",valor)