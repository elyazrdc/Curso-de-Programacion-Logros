cesta_de_compra = [] # Aquí se almacenarán los elementos de la cesta (cada elemento será una lista [nombre, precio])

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
        item_nombre = input("Ingresa el nombre del elemento a agregar: ")
        if item_nombre:
            precio_valido = False
            item_precio = 0.0 # Inicializar para asegurar que tiene un valor
            while not precio_valido:
                precio_str = input(f"Ingresa el precio de '{item_nombre}': ")
                # Comprobar si la entrada es un número válido (entero o flotante)
                if precio_str.replace('.', '', 1).isdigit(): # Permite un solo punto decimal
                    item_precio = float(precio_str)
                    if item_precio >= 0: # Asegurarse de que el precio no sea negativo
                        precio_valido = True
                    else:
                        print("El precio no puede ser negativo. Intenta de nuevo.")
                else:
                    print("Entrada de precio no válida. Por favor, ingresa un número.")

            cesta_de_compra.append([item_nombre, item_precio]) # Guardamos el nombre y el precio juntos
            print(f"'{item_nombre}' con precio ${item_precio:.2f} ha sido añadido a tu cesta.")
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
                # Ahora cada elemento es una lista [nombre, precio]
                nombre = cesta_de_compra[i-1][0]
                precio = cesta_de_compra[i-1][1]
                print(f"{i}. {nombre} - ${precio:.2f}")
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
                nombre = cesta_de_compra[i-1][0]
                precio = cesta_de_compra[i-1][1]
                print(f"{i}. {nombre} - ${precio:.2f}")
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
                        item_eliminado_info = cesta_de_compra.pop(indice) # Pop devuelve la lista [nombre, precio]
                        print(f"'{item_eliminado_info[0]}' ha sido eliminado de tu cesta.")
                        elemento_valido = True # Para salir del bucle interno
                    else:
                        print("Número de elemento inválido. Por favor, ingresa un número dentro del rango.")
                else:
                    print("Entrada no válida. Por favor, ingresa un número.")

    elif opcion == '4':
        # Calcular el total
        if not cesta_de_compra:
            print("La cesta está vacía, no hay total que calcular.")
        else:
            print("\n--- Calculando el Total ---")
            total = 0.0
            i = 0
            while i < len(cesta_de_compra):
                total += cesta_de_compra[i][1] # Sumamos el precio del segundo elemento de la sublista
                i += 1
            print(f"El total de tu compra es: ${total:.2f}")
            print("---------------------------")

    elif opcion == '5':
        # Salir del programa
        print("¡Gracias por usar la aplicación de la cesta de compra! ¡Hasta luego!")
        opcion_salir = True # Cambiar la bandera para terminar el bucle principal

    else:
        # Opción no válida
        print("Opción no válida. Por favor, elige un número del 1 al 5.")