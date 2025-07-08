const displayValorAnterior = document.getElementById('valor-anterior');
const displayValorActual = document.getElementById('valor-actual');
const botonNum = document.querySelectorAll('.num');
const botonOp = document.querySelectorAll('.operador');
const botonSci = document.querySelectorAll('.scientific');

class Calculadora {
    sumar(num1, num2) {
        return num1 + num2;
    }
    resta(num1, num2) {
        return num1 - num2;
    }
    multiplicacion(num1, num2) {
        return num1 * num2;
    }
    division(num1, num2) {
        return num1 / num2;
    }
    modulo(num1, num2) {
        return num1 % num2;
    }
}

class Display {
    constructor(displayValorAnterior, displayValorActual) {
        this.displayValorActual = displayValorActual;
        this.displayValorAnterior = displayValorAnterior;
        this.caculador = new Calculadora();
        this.operacion = undefined;
        this.valorActual = '';
        this.valorAnterior = '';
        this.signos = {
            sumar: '+',
            dividir: '÷',
            restar: '-',
            multiplicar: 'x',
        }
    }

    borrar() {
        this.valorActual = this.valorActual.toString().slice(0,-1);
        this.imprimirValores();
    }

    borrarTodo() {
        this.valorActual = '';
        this.valorAnterior = '';
        this.operacion = undefined;
        this.imprimirValores();
    }
    agregarNum(num) {
        if (num === '.' && this.valorActual.includes('.')) {
            return
        }
        this.valorActual = this.valorActual.toString() + num.toString();
        this.imprimirValores();
    }

    imprimirValores() {
        this.displayValorActual.textContent = this.valorActual;
        this.displayValorAnterior.textContent = `${this.valorAnterior} ${this.signos[this.operacion] || ''}` ;
    }
    calcular() {
        const valorAnterior = parseFloat(this.valorAnterior);
        const valorActual = parseFloat(this.valorActual);

        if (isNaN(valorActual) || isNaN(valorAnterior)) return
        this.valorActual = this.calculador[this.operacion](valorAnterior, valorActual)
    }
    computar(tipo) {
        this.operacion !== 'igual' && this.calcular();
        this.operacion = tipo;
        this.valorAnterior = this.valorActual || this.valorAnterior;
        this.valorActual = '';
        this.imprimirValores();
    }
}

const calculadora = new Calculadora();
const display = new Display(displayValorAnterior, displayValorActual);

console.log(calculadora.sumar(2,3))

botonNum.forEach(btn => {
    btn.addEventListener("click", ()=>{
        display.agregarNum(btn.innerHTML);
    })
})

botonOp.forEach(btn => {
    btn.addEventListener("click", () => {
        display.computar(btn.value);
    })
}) 