#!/usr/bin/node

const axios = require('axios').default;
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
let text = '';
axios.get(url)
  .then(function (datos) {
    text = datos.data;
    fs.writeFile(file, text, 'utf-8', error => {
      if (error) { console.log(error); }
    });
  });
