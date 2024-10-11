function operacion() {
    let n1 = parseFloat(document.getElementById("n1").value);
    let n2 = parseFloat(document.getElementById("n2").value);
    let tipoOpe = document.getElementById("tipo").value;
    let resultado = document.getElementById("resultado");

    if (isNumber(n1) && isNumber(n2)) {
        let ope;

        switch (tipoOpe) {
            case "+":
                ope = n1 + n2;
                break;
            case "-":
                ope = n1 - n2;
                break;
            case "*":
                ope = n1 * n2;
                break;
            case "/":
                if (n2 !== 0) {
                    ope = n1 / n2;
                } else {
                    ope = "Error: División por cero";
                }
                break;
            default:
                ope = "Operación no válida";
                break;
        }

        resultado.innerHTML = `<h2>${n1} ${tipoOpe} ${n2} = ${ope}</h2>`;
    } else {
        alert("Ingresa solo números");
    }
}

function isNumber(n) {
    return !isNaN(parseFloat(n)) && isFinite(n);
}
