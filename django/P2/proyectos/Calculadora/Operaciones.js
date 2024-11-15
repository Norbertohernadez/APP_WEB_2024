function calculate() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);
    const operation = document.getElementById('operation').value;
    let result;

    switch (operation) {
        case 'add':
            result = num1 + num2;
            break;
        case 'subtract':
            result = num1 - num2;
            break;
        case 'multiply':
            result = num1 * num2;
            break;
        case 'divide':
            result = num2 !== 0 ? num1 / num2 : 'Error: Dividir entre cero';
            break;
        default:
            result = 'Operación no válida';
    }

    document.getElementById('result').innerText = `Resultado: ${result}`;
}

function showInputs() {
    const figure = document.getElementById('figure').value;
    const inputs = document.getElementById('inputs');
    inputs.innerHTML = '';

    switch (figure) {
        case 'triangle':
            inputs.innerHTML = `
                <input type="number" id="base" placeholder="Base">
                <input type="number" id="height" placeholder="Altura">
            `;
            break;
        case 'circle':
            inputs.innerHTML = `
                <input type="number" id="radius" placeholder="Radio">
            `;
            break;
        case 'square':
            inputs.innerHTML = `
                <input type="number" id="side" placeholder="Lado">
            `;
            break;
        case 'rectangle':
            inputs.innerHTML = `
                <input type="number" id="length" placeholder="Largo">
                <input type="number" id="width" placeholder="Ancho">
            `;
            break;
    }
}

function calculateArea() {
    const figure = document.getElementById('figure').value;
    let area;
    let imageUrl = ''; 

    switch (figure) {
        case 'triangle':
            const base = parseFloat(document.getElementById('base').value);
            const height = parseFloat(document.getElementById('height').value);
            area = (base * height) / 2;
            imageUrl = 'area-triangulo.png';
            break;
        case 'circle':
            const radius = parseFloat(document.getElementById('radius').value);
            area = Math.PI * radius * radius;
            imageUrl = 'circulo.png'; 
            break;
        case 'square':
            const side = parseFloat(document.getElementById('side').value);
            area = side * side;
            imageUrl = 'cuadrado.png'; 
            break;
        case 'rectangle':
            const length = parseFloat(document.getElementById('length').value);
            const width = parseFloat(document.getElementById('width').value);
            area = length * width;
            imageUrl = 'rectangulo.png';
            break;
        default:
            area = 'Figura no seleccionada';
            imageUrl = 'selecciona.jpg';
    }

    document.getElementById('areaResult').innerText = `Área: ${area}`;
    document.getElementById('figureImage').innerHTML = imageUrl ? `<img src="${imageUrl}" alt="${figure}">` : '';
}

