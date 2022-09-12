#!/usr/bin/node

const axios = require('axios').default;
const id = process.argv[2];
axios.get('https://swapi-api.hbtn.io/api/films/' + id)
  .then((response) => {
    console.log(response.data.title);
  });
