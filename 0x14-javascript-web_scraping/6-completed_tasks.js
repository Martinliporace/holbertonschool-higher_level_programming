#!/usr/bin/node

const axios = require('axios').default;
const url = process.argv[2];

axios.get(url)
  .then(function (datos) {
    const elements = datos.data;
    const table = {};
    const largo = elements.length;
    for (let i = 0; i < largo; i++) {
      if (elements[i].completed === true) {
        if (table[elements[i].userId] !== undefined) {
          table[elements[i].userId] = table[elements[i].userId] += 1;
        } else {
          table[elements[i].userId] = 1;
        }
      }
    }
    console.log(table);
  });
