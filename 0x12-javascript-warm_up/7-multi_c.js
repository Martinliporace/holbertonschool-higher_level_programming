#!/usr/bin/node
const arg = process.argv[2];
const text = 'C is fun';
let toPrint = parseInt(arg);

if (isNaN(toPrint)) {
  console.log('Missing number of occurrences');
} else {
  while (toPrint > 0) {
    console.log(text);
    toPrint--;
  }
}
