#!/usr/bin/node

const axios = require('axios').default;
const id = process.argv[2];
const urls = [];

axios.get('https://swapi-api.hbtn.io/api/films/' + id)
  .then((response) => {
    const chars = (response.data.characters);
    for (let i = 0; i < chars.length; i++) { urls.push(chars[i]); }

    urls.forEach(element => axios.get(element)
      .then((response) => {
        const name = (response.data.name);
        console.log(name);
      }));
  });
