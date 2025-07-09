//Ejercicio 10: Constantes const y Funciones void
//Crea un programa para calcular el perímetro de un círculo.
//- Declara una constante de tipo double usando la palabra clave const para el valor de Pi (π≈3.14159).
//- Escribe una función void llamada calcularPerimetro que no devuelva ningún valor pero que reciba como parámetro el radio del círculo.
//- Dentro de esta función, calcula el perímetro (2⋅π⋅radio) y muéstralo directamente en la consola.
//- Desde main, pide al usuario el radio y llama a la función calcularPerimetro.

#include<cmath>
#include<iostream>

int calcularPerimetro(int radio) {
    double pi = M_PI;
    int perimetro = 2*pi*radio;
    return perimetro;
}

int main() {
    int radio;
    std::cout << "Dime el radio de un circulo\n";
    std::cin >> radio;
    int perimetroCirculo = calcularPerimetro(radio);
    std::cout << "\nEl perimetro del radio es " << perimetroCirculo;
    return 0;
}