#include <iostream> // Necesario para la entrada/salida (como cout)
#include <string>   // Necesario para usar std::string (aunque para un solo char no es estrictamente necesario, es buena práctica si vas a usar cadenas)

int main() {
    // Imprimir el mensaje "¡Hola, Mundo!"
    std::cout << "¡Hola, Mundo!" << std::endl;

    // ---

    // Declaración e inicialización de variables para diferentes tipos de datos

    // Entero (int)
    // Un número entero, sin parte decimal.
    int miEntero = 10;

    // Flotante (float)
    // Un número con parte decimal, con menor precisión que double.
    float miFlotante = 3.14f; // La 'f' al final indica que es un float, no un double por defecto

    // Carácter (char)
    // Un solo carácter. Se encierra entre comillas simples.
    char miCaracter = 'A';

    // Booleano (bool)
    // Un valor que puede ser true (verdadero) o false (falso).
    bool miBooleano = true;

    // Opcional: Imprimir los valores para verificación
    std::cout << "Mi entero: " << miEntero << std::endl;
    std::cout << "Mi flotante: " << miFlotante << std::endl;
    std::cout << "Mi caracter: " << miCaracter << std::endl;
    std::cout << "Mi booleano: " << miBooleano << std::endl; // true se imprime como 1, false como 0

    return 0; // Indica que el programa se ejecutó correctamente
}