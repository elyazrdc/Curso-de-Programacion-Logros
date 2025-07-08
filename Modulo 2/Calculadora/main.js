document.addEventListener('DOMContentLoaded', function() {
            const display = document.getElementById('display');
            const buttons = document.querySelectorAll('button');
            let currentInput = '0';
            let lastOperation = null;
            
            // Función para actualizar el display
            function updateDisplay() {
                display.textContent = currentInput;
            }
            
            // Función para validar expresiones matemáticas
            function isValidMathExpression(expr) {
                try {
                    // Intenta evaluar la expresión para ver si es válida
                    new Function('return ' + expr);
                    return true;
                } catch {
                    return false;
                }
            }
            
            // Función para calcular el resultado
            function calculateResult() {
                try {
                    // Reemplazar símbolos matemáticos para evaluación
                    let expr = currentInput
                        .replace(/×/g, '*')
                        .replace(/÷/g, '/')
                        .replace(/\^/g, '**')
                        .replace(/√\(([^)]+)\)/g, 'Math.sqrt($1)')
                        .replace(/sin\(([^)]+)\)/g, 'Math.sin($1)')
                        .replace(/cos\(([^)]+)\)/g, 'Math.cos($1)')
                        .replace(/tan\(([^)]+)\)/g, 'Math.tan($1)');
                    
                    if (isValidMathExpression(expr)) {
                        const result = new Function('return ' + expr)();
                        if (Number.isFinite(result)) {
                            currentInput = String(result % 1 === 0 ? result : parseFloat(result.toFixed(8)));
                        } else {
                            currentInput = 'Error';
                        }
                    } else {
                        currentInput = 'Error';
                    }
                } catch (error) {
                    currentInput = 'Error';
                }
                updateDisplay();
            }
            
            buttons.forEach(button => {
                button.addEventListener('click', function() {
                    const buttonValue = this.textContent;
                    const buttonId = this.id;
                    
                    switch(buttonId) {
                        case 'ac':
                            currentInput = '0';
                            break;
                            
                        case 'de':
                            currentInput = currentInput.length === 1 ? '0' : currentInput.slice(0, -1);
                            break;
                            
                        case '=':
                            calculateResult();
                            break;
                            
                        case '√':
                            currentInput = currentInput === '0' ? '√(' : currentInput + '√(';
                            break;
                            
                        case '^':
                            currentInput += '^';
                            break;
                            
                        case 'sin':
                            currentInput = currentInput === '0' ? 'sin(' : currentInput + 'sin(';
                            break;
                            
                        case 'cos':
                            currentInput = currentInput === '0' ? 'cos(' : currentInput + 'cos(';
                            break;
                            
                        case 'tan':
                            currentInput = currentInput === '0' ? 'tan(' : currentInput + 'tan(';
                            break;
                            
                        case '.':
                            // Evitar múltiples puntos decimales en un número
                            const parts = currentInput.split(/[\+\-\*\/]/);
                            if (!parts[parts.length - 1].includes('.')) {
                                currentInput += '.';
                            }
                            break;
                            
                        default:
                            if (currentInput === '0' && buttonId !== '.') {
                                currentInput = buttonValue;
                            } else {
                                currentInput += buttonValue;
                            }
                    }
                    
                    updateDisplay();
                });
            });
        });