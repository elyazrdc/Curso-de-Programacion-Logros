//📐 Ejercicio 7: Funciones con Valor de Retorno
//Desarrolla un programa que contenga una función llamada calcularAreaRectangulo.
//- Declara (Prototipo) la función al inicio del programa.
//- La función debe recibir dos parámetros de tipo float: la base y la altura.
//- La función debe devolver el área calculada.
//- Desde la función main, solicita al usuario la base y la altura, llama a la función y muestra el resultado.

#include<iostream>

int calcularAreaRectangulo(float base, float altura) {
    float areaCalculada = base * altura;
    return areaCalculada;
}

int main() {
    float a;
    float b;

    std::cout << "Dame la base de un rectangulo\n";
    std::cin  >> a;
    std::cout << "Dame la altura de un rectangulo\n";
    std::cin >> b;
    float resultado = calcularAreaRectangulo(a,b);
    
    std::cout << "El area del rectangulo es " << resultado << std::endl;

    return 0;
}
