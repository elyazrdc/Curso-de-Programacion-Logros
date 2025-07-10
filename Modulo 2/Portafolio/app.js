const typing = document.getElementById("typing");
const fullText = "desarrollador Web";
let charIndex = 0;
const delayAfterType = 3000;
const delayAfterErase = 500;
const eraseSpeed = 50;

function typeWriter() {
    if (charIndex < fullText.length) {
        // Añade el siguiente carácter al contenido del párrafo
        typing.textContent += fullText.charAt(charIndex);
        charIndex++; // Pasa al siguiente carácter
        setTimeout(typeWriter, 100); // Llama a la función de nuevo después de 100 milisegundos (0.1 segundos)
    }
    else {
        setTimeout(eraseText, delayAfterType)
    }
}

 function eraseText() {
            if (charIndex > 0) {
                // Borrando
                typing.textContent = fullText.substring(0, charIndex - 1);
                charIndex--;
                setTimeout(eraseText, eraseSpeed);
            } else {
                // Texto borrado, espera un momento y vuelve a escribir
                setTimeout(typeWriter, delayAfterErase);
            }
        }

// Inicia el efecto cuando la página carga
document.addEventListener('DOMContentLoaded', typeWriter);