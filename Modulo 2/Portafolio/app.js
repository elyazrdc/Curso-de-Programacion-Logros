const typing = document.getElementById("typing");
const fullText = "desarrollador Web";
let charIndex = 0;
const delayAfterType = 3000;
const delayAfterErase = 500;
const eraseSpeed = 50;

// BOTONES DEL ASIDE

asideItem = document.querySelectorAll('.aside-item');

// btnAbout = document.getElementById('about-link');
// btnHome = document.getElementById('home-link')
// btnService = document.getElementById('service-link');
// btnPortfolio = document.getElementById('portfolio-link');
// btnContact = document.getElementById('contact-link');

sectionArray = document.querySelectorAll('.section');

// sectionAbout = document.getElementById('about-section');
// sectionHome = document.getElementById('home-section');
// sectionService = document.getElementById('service-section');
// sectionPortfolio = document.getElementById('portfolio-section');
// sectionContact = document.getElementById('contact-section');
// sectionArray = []
// sectionArray.push(sectionHome, sectionAbout,sectionService,sectionPortfolio,sectionContact);
// console.log(sectionArray);

asideItem.forEach((element) => {
    element.addEventListener("click", () => {
        clickedItem = element.id;
        targetSectionId = clickedItem.replace('-link', '-section');
        const targetSection = document.getElementById(targetSectionId);

        asideItem.forEach(item => {
            item.classList.remove('active');
        });
        element.classList.add('active');

        sectionArray.forEach(section => {
            section.classList.add('hidden');
            setTimeout(() => {
                section.classList.add('hidden-complete');
            }, 900);
        });

        targetSection.classList.remove('hidden');

        setTimeout(() => {
            targetSection.classList.remove('hidden-complete');
        }, 900);
    })
});

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