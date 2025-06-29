# Ejercicio 1

edad=int(input("por favor, coloca tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Ejercicio 2
valor=int(input("ingrese un numeropara comprobar que sea positivo, negativo o igual a 0: "))
if valor>0:
    print(f"El  numero {valor} es positivo ")
elif valor==0:
    print(f"El  numero ingresado es igual a 0 ")
else:
    print(f"El  numero {valor} es negativo ")
    
# Ejercicio 3
print("Vamos a comparar dos numeros")
numero1 = int(input("Por favor, coloca el primer numero: "))
numero2 = int(input("Por favor, coloca el segundo numero: "))

if numero1 > numero2:
    print("El primer numero es mayor que el segundo")
elif numero1 < numero2:
    print("El segundo numero es mayor que el primero")
else:        
    print("Los numeros son iguales")
    
# Ejercicio 4
print("Comprobar si un año es bisiesto o no")

año=int(input("Por favor, coloca un año: "))
if (año %4==0 and año %100 !=0 ) or año%400==0 :
    print(f"el año {año} es bisiesto")
else:
    print(f"el año {año} no es bisiesto")
    
# Ejercicio 5
print("vamos a calcular el descuento de un poducto")

precio_original=int(input("Ingrese el precio original del producto: "))
descuento=int(input("Ingrese el descuento del producto (solo el numero): "))
descuento_porcentual=descuento/100
descuento_antes=precio_original*descuento_porcentual
descuento_final=precio_original-descuento_antes
print(f"el producto tiene un descuento de: {descuento_antes} $")
print(f"el precio final es de: {descuento_final} $")

# Ejercicio 6

print("Operaciones matematicas")
A=int(input("ingrese el primer numero: "))
B=int(input("ingrese el segundo numero: "))


suma = A+B
divi =A/B
divi_ent =A//B
modulo = A%B
resta = A-B
multi= A*B
exp= A**B

print("El resultado de la operacion suma :",suma)
print("El resultado de la operacion division :",divi)
print("El resultado de la operacion division entera :",divi_ent)
print("El resultado de la operacion modulo :",modulo)
print("El resultado de la operacion resta :",resta)
print("El resultado de la operacion exponecial :",exp)
print("El resultado de la operacion multiplicacion :",multi)

# Ejercicio 7
print("Verificar si un numero esta ente un rango de numero")
rango_a=int(input("ingrese un numero para determinar un limite: "))
rango_b=int(input("ingrese otro numero para determinar un limite: "))
if rango_a==rango_b:
    print("los numero son iguales")

else:
    dato=int(input(f"veamos si este numero se encuentra en el rango de {rango_a} y {rango_b}:  "))
   
    if (rango_a<dato<rango_b) or (rango_b<dato<rango_a) :
        print(f"el numero {dato} se encuentra en el rango de valores! ")
    else:
        print(f"el numero {dato} no se encuentra en el rango de valores! ")
        
# Ejercicio 8
print("Por favor ingresa tus datos:")

nombre = input("Nombre: ")
edad = input("Edad: ")
ciudad = input("Ciudad: ")

print("\nInformación ingresada:")
print(f"nombre:{nombre},edad:{edad},ciudad:{ciudad}")

# Ejercicio 9
print("Vamos a realizar una suma")
A=int(input("ingrese el primer numero: "))
B=int(input("ingrese el segundo numero: "))

suma = A+B

print("El resultado de la operacion suma :",suma)

# Ejercicio 10
print("Vamos a verificar si dos numeros son mayores que 10  ")
range_a=int(input("ingrese un numero para determinar: "))
range_b=int(input("ingrese otro numero para determinar: "))
verificacion=range_a>10 and range_b>10
if range_a>10 and range_b>10:
    print(verificacion)

else:
    print(verificacion)

# Ejercicio 11
print("Vamos a verificar si un numeros es mayor que los otros dos  ")
range_a=int(input("ingrese el primer numero para determinar: "))
range_b=int(input("ingrese el segundo numero para determinar: "))
range_c=int(input("ingrese el tercer numero para determinar: "))

if range_a>rango_b>range_c:
    print(f"{range_a} es mayor que  {range_b} y, {range_b} es mayor que {range_c}")
else:
    print(f" no es mayor que alguno de los numeros ingresados")
    
# Ejercicio 12
verdad=True
mentira=False
verdad_false=not verdad
print("verdad",verdad)
print("mentira",mentira)
print(f"verdad con not:{verdad_false}")

# Ejercicio 13
dato=int(input(f"veamos si este numero se encuentra en el rango de 20 y 50:  "))
   
if (20<dato<50):
    print(f"el numero {dato} se encuentra en el rango de valores! ")
else:
    print(f"el numero {dato} no se encuentra en el rango de valores! ")

# Ejercicio 14

nota=int(input("Ingrese su nota: "))

if 90<=nota<=100:
    print("tu calificacion es: A")
elif 80<=nota<90:
    print("tu calificacion es: B")
elif 70<=nota<80:
    print("tu calificacion es: C")
elif 60<=nota<70:
    print("tu calificacion es: D")
else:
    print("tu calificacion es: F")

# Ejercicio 15
valor=int(input("ingrese un numeropara comprobar que sea positivo, negativo o igual a 0: "))
opcion=0
if valor>0:
    print(f"El  numero {valor} es positivo ")
elif valor==0:
    print(f"El  numero ingresado es igual a 0 ")
else:
    print(f"El  numero {valor} es negativo ")