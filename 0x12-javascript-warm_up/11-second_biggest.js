#!/usr/bin/node
const len = process.argv.length;
let i = 2;
let j = 2;
let mayor = parseInt(process.argv[i]);
let segundo = parseInt(process.argv[j]);

if (isNaN(process.argv[2]) || isNaN(process.argv[3])) {
  console.log(0);
} else {
  while (i < len) {
    if (mayor < parseInt(process.argv[i + 1])) {
      mayor = parseInt(process.argv[i + 1]);
    } i++;
  }
  const big = mayor;
  while (j < len) {
    if (segundo < parseInt(process.argv[j + 1]) && parseInt(process.argv[j + 1]) < big) {
      segundo = parseInt(process.argv[j + 1]);
    } j++;
  }
  console.log(segundo);
}
