#!/usr/bin/node
const arg = process.argv[2];
const text = 'X';
const toPrint = parseInt(arg);

if (isNaN(toPrint)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < toPrint; i++) {
    for (let j = 0; j < toPrint; j++) {
      process.stdout.write(text);
    }
    console.log('');
  }
}
