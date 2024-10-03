function manuFeacture(regalos, materiales) {
    materiales = materiales.toLowerCase();

    let palabra = '';
    let nuevosRegalos = [];

    for (let i = 0; i < regalos.length; i++) {
        const regalo = regalos[i].split('')
        for (let j = 0; j < regalo.length; j++) {
            const caracter = regalo[j].toLowerCase();
            if (materiales.includes(caracter)) {
                palabra += caracter;
            }
        }

        if (palabra === regalos[i]) {
            nuevosRegalos.push(palabra);
        }

        palabra = '';
    }

    return nuevosRegalos

}

const obsequios = ["libro", 'ps5'];
const materiales = 'psli';


const letras = "abcde"


console.log(manuFeacture(obsequios, materiales))