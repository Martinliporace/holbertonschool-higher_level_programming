#!/usr/bin/node
const arg = process.argv[2];
const toPrint = parseInt(arg);
if (isNaN(toPrint)) {
  console.log('Not a number');
} else {
console.log(toPrint);
}
