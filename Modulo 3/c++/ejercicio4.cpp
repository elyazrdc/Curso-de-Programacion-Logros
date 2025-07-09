// Bucle for y Constantes con #define
// Utiliza #define para crear una constante simbólica llamada LIMITE con un valor de 10. Luego, escribe un programa que pida al usuario un número y utilice un bucle for para imprimir la tabla de multiplicar de ese número desde 1 hasta LIMITE.

#include<iostream>

int main() {
    int LIMITE = 10;
    int numero;
    std::cout << "Dime un numero\n";
    std::cin >> numero;
    for (int i = 1; i <= LIMITE; i++) {
        std::cout <<  numero << "x" << i << "=" << numero*i << std::endl;
    }
    
    return 0;
}