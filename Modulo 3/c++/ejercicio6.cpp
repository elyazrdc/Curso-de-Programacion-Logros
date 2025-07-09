//Ejercicio 6: Bucle do-while y switch
//Escribe un programa que muestre un menú simple con tres opciones:
//1. Saludar
//2. Despedirse
//3. Salir

//El programa debe usar un bucle do-while para mostrar el menú repetidamente hasta que el usuario elija la opción "Salir". Utiliza una estructura switch para manejar la opción seleccionada por el usuario y mostrar el mensaje correspondiente.

#include<iostream>

int main() {
    int option;

    do {
        std::cout << "\nEscoge una opcion";
        std::cout << "\n1 Saludar";
        std::cout << "\n2 Despedirse";
        std::cout << "\n3 Salir";
        std::cout << "\n";

        std::cin  >> option;

        switch (option) {
            case 1:
                std::cout << "\nHola manolo";
                break;
            case 2:
                std::cout << "\nAdios manolo";
                break;
            case 3:
                std::cout << "\nNos vemo";
                break;
            default:
                std::cout << "Opcion no valida";
                break;
        }
    } while (option != 3);
    
    return 0;
}