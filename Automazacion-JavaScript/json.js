const fs= require('fs');


//lee la informacion del json

let jsonData = require('./JSON/registro.json');
console.log(jsonData);

//jsonData.NumeroObjetos=jsonData.NumeroObjetos+1;
nuevaFecha='fecha-nuevqa';
nuevoValor=[]
jsonData.registros.push(nuevoValor);
jsonData.registros[jsonData.NumeroObjetos].fecha=nuevaFecha;

console.log(jsonData.registros[1].fecha);

//NuevoJason=jsonData;

//console.log(NuevoJason);
//console.log(typeof(NuevoJason));


//escribe informacion en el json