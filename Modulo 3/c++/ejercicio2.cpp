// Incluimos la librería iostream para poder usar cout y cin
//Crea un programa que solicite al usuario dos números. El programa debe calcular y mostrar:
// - La suma, resta, multiplicación y división de los dos números.
// - Utilizando la librería <cmath>, calcula y muestra la potencia del primer número elevado al segundo y la raíz cuadrada del primer número.

#include <iostream> // Needed for std::cout and std::cin
#include <cmath>    // Needed for std::pow and std::sqrt (if you add it)

int main() {
    double num1; // Use double for better precision in calculations
    std::cout << "Introduce numero uno: ";
    std::cin >> num1;

    double num2; // Use double for better precision
    std::cout << "Introduce numero dos: ";
    std::cin >> num2;

    // --- Basic Operations ---
    std::cout << "\n--- Calculation Results ---\n";
    std::cout << "Suma: " << num1 + num2 << std::endl;
    std::cout << "Resta: " << num1 - num2 << std::endl;
    std::cout << "Multiplicacion: " << num1 * num2 << std::endl;

    // Handle division by zero
    if (num2 != 0) {
        std::cout << "Division: " << num1 / num2 << std::endl;
    } else {
        std::cout << "Division: Cannot divide by zero." << std::endl;
    }

    // --- Power Calculation using cmath ---
    double resultado_potencia = std::pow(num1, num2);
    std::cout << "Potencia (" << num1 << " elevado a " << num2 << "): " << resultado_potencia << std::endl;

    return 0; // Indicates successful program execution
}