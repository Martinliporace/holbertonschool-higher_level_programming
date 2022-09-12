#!/usr/bin/node

const axios = require('axios').default;
const url = process.argv[2];
let cont = 0;
let total = 0;
axios.get(url)
  .then(function (datos) {
    total = datos.data.count;
    for (let i = 0; i < total; i++) {
      const chars = datos.data.results[i];
      const cant = chars.characters.length;
      for (let j = 0; j < cant; j++) {
        if (chars.characters[j].includes('/18/')) {
          cont++;
        }
      }
    }
    console.log(cont);
})
  .catch(function (error) {
    if (error.response) {
      console.log('code: ' + error.response.status);
    }

  });
