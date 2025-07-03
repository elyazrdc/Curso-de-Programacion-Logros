
<?php
//Escribe un script que cuente y muestre la cantidad de números pares e impares que hay en el rango del 1 al 50.

for ($i=0; $i <= 50; $i++) { 
    if ($i % 2 == 0) {
        echo "\nnumero par: " . $i;
    }
    else if($i % 2 == 1) {
        echo "\nnumero impar: " . $i;
    }
}


//Crea un script que genere y muestre en la terminal la tabla de multiplicar completa del número 8, desde el 8x1 hasta el 8x10.
echo "TABLA DEL 8";
for ($i=1; $i <= 10; $i++) { 
    echo "\n8 x " . $i . " = " . (8*$i);
}


//Desarrolla un programa que simule un juego de "adivina el número". Define una variable con un número secreto y utiliza un bucle while para "intentar" adivinarlo incrementando un contador hasta encontrarlo, mostrando cada intento.
$adivina = 3;
$intentos = 3;
echo "Adivina un numero del uno al 10";

while ($adivina != 7 && $intentos != 0) {
    
    echo "\nNumero equivocado, intenta otra vez";
    $intentos--;
}
if ($intentos == 0) {
        echo "\nIntentos agotados, suerte la proxima";
}

//Escribe un script que calcule la suma de todos los números impares desde el 1 hasta el 100.
$suma = 0;

for ($i=1; $i <= 100 ; $i++) { 
    if ($i % 2 == 1) {
        $suma += $i;
    }
}
echo "La suma todos los numeros impares del 1 al 100 es: " . $suma;

//Crea un programa que verifique si una persona puede obtener una licencia de conducir. La condición es que debe tener al menos 18 años y no más de 65 años. Define una variable para la edad y muestra si cumple los requisitos o no.

//Utilizando bucles anidados, crea un script que dibuje un cuadrado de 5x5 en la terminal utilizando el carácter #.

for ($i=0; $i < 5; $i++) { 
    for ($e=0; $e < 5; $e++) { 
       echo "# "; 
    }
    echo "\n";
}


//Desarrolla un script que determine si un número almacenado en una variable es positivo, negativo o cero y muestre el resultado.

$variable = 2;
var_dump($variable);


//Escribe un programa que imprima los números del 1 al 30. Para los múltiplos de 3, debe imprimir "Mar" en su lugar. Para los múltiplos de 5, debe imprimir "Tierra". Para los múltiplos de ambos (3 y 5), debe imprimir "MarTierra".

for ($i=1; $i <= 30; $i++) { 
    if ($i % 3 == 0) {
        echo "\nMar";
    }
    else if ($i % 5 == 0) {
        echo "\nTierra";
    }
    else if ($i % 5 == 0 && $i % 3 == 0) {
        echo "\nMarTierra";
    }
}

//Crea un script que, dada una variable numérica que representa la temperatura en grados Celsius, muestre un mensaje diferente si la temperatura es "fría" (menos de 10°C), "templada" (entre 10°C y 25°C) o "calurosa" (más de 25°C).

$temp = 18;
if ($temp > 10 && $temp < 25) {
    echo "Temperatura templada";
} else if ($temp < 10) {
    echo "Temperatura fria";
} else if ($temp > 25) {
    echo "Temperatura calurosa";
}

//Escribe un programa que realice una cuenta regresiva para Año Nuevo desde el 10 hasta el 1. Al final, debe mostrar el mensaje "¡Feliz Año Nuevo!".

for ($i = 10; $i >= 0; $i--) {
    echo $i . "\n";
    if ($i == 0) {
        echo "FELIZ AÑO NUEVO\n";
    }
}
?>