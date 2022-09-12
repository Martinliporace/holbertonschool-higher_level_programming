#!/usr/bin/node

const fs = require('fs');
const text = process.argv[2];
fs.readFile(text, 'utf8', (error, datos) => {
  if (error) { console.log(error); } else { console.log(datos.toString()); }
});
