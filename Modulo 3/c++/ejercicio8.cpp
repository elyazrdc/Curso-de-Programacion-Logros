//Ejercicio 8: Paso por Valor vs. Paso por Referencia
//Crea un programa que demuestre la diferencia entre el paso por valor y el paso por referencia.
//- Define una función void llamada modificarPorValor que reciba un entero por valor y le sume 10 dentro de la función.
//- Define otra función void llamada modificarPorReferencia que reciba un entero por referencia y le sume 10.
//- En main, declara una variable entera llamada numero e inicialízala en 20. Imprime su valor, llama a modificarPorValor, vuelve a imprimir numero. Luego, llama a modificarPorReferencia y vuelve a imprimir el valor de numero para observar la diferencia.

#include<iostream>

int modificarPorValor(int valor) {
   int suma = valor + 10;
   return suma;
}

int modificarPorReferencia(int valor) {
    int suma = valor +10;
    return suma;
}

int main() {
    int numero = 20;
    std::cout << "\nValor del numero " << numero;
    int numero2 = modificarPorValor(numero);
    std::cout << "\nValor del numero modificado por valor " << numero2;
    int numero3 = modificarPorReferencia(numero2);
    std::cout << "\nValor del numero modificador por referencia " << numero3;
    return 0;
}