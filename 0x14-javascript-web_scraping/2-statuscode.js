#!/usr/bin/node

const axios = require('axios').default;
const target = process.argv[2];
axios
  .get(target)
  .then((response) => {
    console.log('code: ' + response.status);
  })
  .catch(function (error) {
    if (error.response) {
      console.log('code: ' + error.response.status);
    }
  });
