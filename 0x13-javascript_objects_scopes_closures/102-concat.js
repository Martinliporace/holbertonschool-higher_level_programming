#!/usr/bin/node
const output = require('fs');
const textOne = output.readFileSync(process.argv[2]);
const textTwo = output.readFileSync(process.argv[3]);
output.writeFileSync(process.argv[4], textOne + textTwo);
