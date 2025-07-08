// Ejercicio 3: Condicionales if-else
// Desarrolla un programa que pida al usuario su edad.
// El programa debe utilizar una estructura condicional if-else para determinar si el usuario es mayor de edad (18 años o más) y mostrar un mensaje apropiado en la pantalla.

#include <iostream>
#include <string>

int main() {
    std::cout << "Dime tu edad ";
    int edad;
    std::cin >> edad;
    
    if (edad > 18) {
        std::cout << "Eres mayor de edad";
    }
    else {
        std::cout << "Eres menor de edad";
    }
    
    return 0;
}