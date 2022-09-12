#!/usr/bin/node

const axios = require('axios').default;
const url = process.argv[2];
let cont = 0;
let total = 0;
axios.get(url)
  .then(datos => {
    total = datos.data.count;
    for (let i = 0; i < total; i++) {
      const chars = datos.data.results[i];
      const cant = chars.characters.length;
      for (let j = 0; j < cant; j++) {
        if (chars.characters[j].includes('18')) {
          cont++;
          break;
        }
      }
    }
    console.log(cont);
  })
.catch(function (error) {
    console.log(`code: ${error.response.status}`);
  });
