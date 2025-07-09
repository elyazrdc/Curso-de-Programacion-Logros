//Crea un programa que simule un juego de adivinanza. El programa debe generar un número secreto (por ejemplo, int numeroSecreto = 42;). Luego, debe pedir al usuario que adivine el número. Utiliza un bucle while para que el programa siga pidiendo un número mientras el usuario no adivine el correcto. Proporciona pistas como "más alto" o "más bajo".

#include<iostream>

int main() {
    int numeroSecreto = 4;
    int numeroAdi;

    do {
        std::cout << "Dime un numero, adivinaremos el numero secreto\n";
        std::cin >> numeroAdi;

        if (numeroSecreto == numeroAdi) {
            std::cout << "ADIVINASTE\n";
        }
        else if (numeroAdi > numeroSecreto) {
            std::cout << "Cerca, es un numero mas bajo\n";
        }
        else if (numeroAdi < numeroSecreto) {
            std::cout << "Cerca, es un numero mas alto\n";
        }
        else {
            std::cout << "No es ese\n";
        }
    } while(numeroSecreto != numeroAdi);

    return 0;
}