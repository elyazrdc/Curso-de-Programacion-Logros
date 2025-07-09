//Ejercicio 9: Librerías vector y string
//Escribe un programa que pida al usuario que ingrese 3 de sus comidas favoritas. Almacena cada comida en un vector de tipo string. Después de que el usuario haya ingresado las tres, utiliza un bucle para recorrer el vector e imprimir cada una de las comidas en la consola.
#include<iostream>
#include<string>
#include<vector>

int main() {
    std::vector<std::string> comidasFavoritas;
    

    for (int i= 0; i<3; i++) {
        std::string comida;
        std::cout << "Ingresa tu comida favorita\n";
        std::cin >> comida;
        comidasFavoritas.push_back(comida);
    }
    std::cout << "Tus comidas favoritas\n";
    for (int i = 0; i < 3; i++) {
        std::cout << "\n" << comidasFavoritas[i];
    }
    return 0;
}