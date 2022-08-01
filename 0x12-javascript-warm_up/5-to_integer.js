#!/usr/bin/node
const arg = process.argv[2];
const toPrint = parseInt(arg);
if (toPrint === null) {
  console.log('Not a number');
} console.log(toPrint);
