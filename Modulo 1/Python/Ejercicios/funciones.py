# Funcion que calcula el area de un circulo

def calcular_area_circulo(radio):
    """Función que calcula el área de un círculo."""
    import math  # Importa el módulo math para usar la constante pi
    return math.pi * (radio ** 2)  # Calcula el área usando la fórmula π * r^2

radio_circulo = int(input("Dime el radio de un circulo: "))
area_circulo = calcular_area_circulo(radio_circulo)
print(f"El area del circulo es: {area_circulo:.2f}")