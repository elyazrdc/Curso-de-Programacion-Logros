cesta_de_compra = [] # Aquí se almacenarán los elementos de la cesta

opcion_salir = False
while not opcion_salir:
    # Mostrar el menú
    print("\n--- Menú de Opciones ---")
    print("1. Agregar un nuevo elemento")
    print("2. Mostrar el contenido de la cesta de la compra")
    print("3. Eliminar un elemento")
    print("4. Calcular el total")
    print("5. Salir")
    print("------------------------")

    opcion = input("Elige una opción (1-5): ")

    if opcion == '1':
        # Agregar un nuevo elemento
        item = input("Ingresa el nombre del elemento a agregar: ")
        if item:
            cesta_de_compra.append(item)
            print(f"'{item}' ha sido añadido a tu cesta.")
        else:
            print("No ingresaste ningún elemento. Intenta de nuevo.")

    elif opcion == '2':
        # Mostrar el contenido de la cesta de la compra
        if not cesta_de_compra:
            print("Tu cesta de compra está vacía.")
        else:
            print("\n--- Contenido de tu Cesta ---")
            i = 1
            while i <= len(cesta_de_compra):
                print(f"{i}. {cesta_de_compra[i-1]}")
                i += 1
            print("-----------------------------")

    elif opcion == '3':
        # Eliminar un elemento
        if not cesta_de_compra:
            print("La cesta está vacía, no hay elementos para eliminar.")
        else:
            # Mostrar cesta para que el usuario elija
            print("\n--- Contenido de tu Cesta ---")
            i = 1
            while i <= len(cesta_de_compra):
                print(f"{i}. {cesta_de_compra[i-1]}")
                i += 1
            print("-----------------------------")
            
            elemento_valido = False
            while not elemento_valido:
                entrada = input("Ingresa el número del elemento a eliminar (o '0' para cancelar): ")
                
                if entrada == '0':
                    print("Eliminación cancelada.")
                    elemento_valido = True # Para salir del bucle interno
                elif entrada.isdigit():
                    indice = int(entrada) - 1 # Convertir a índice de lista (base 0)
                    
                    if indice >= 0 and indice < len(cesta_de_compra):
                        item_eliminado = cesta_de_compra.pop(indice)
                        print(f"'{item_eliminado}' ha sido eliminado de tu cesta.")
                        elemento_valido = True # Para salir del bucle interno
                    else:
                        print("Número de elemento inválido. Por favor, ingresa un número dentro del rango.")
                else:
                    print("Entrada no válida. Por favor, ingresa un número.")

    elif opcion == '4':
        # Calcular el total (simulado)
        if not cesta_de_compra:
            print("La cesta está vacía, no hay total que calcular.")
        else:
            print("\n--- Calculando el Total ---")
            print(f"Tienes {len(cesta_de_compra)} elementos en tu cesta.")
            precio_por_item = 5.0 
            total = len(cesta_de_compra) * precio_por_item
            print(f"El total estimado de tu compra es: ${total:.2f}")
            print("---------------------------")

    elif opcion == '5':
        # Salir del programa
        print("¡Gracias por usar la aplicación de la cesta de compra! ¡Hasta luego!")
        opcion_salir = True # Cambiar la bandera para terminar el bucle principal

    else:
        # Opción no válida
        print("Opción no válida. Por favor, elige un número del 1 al 5.")