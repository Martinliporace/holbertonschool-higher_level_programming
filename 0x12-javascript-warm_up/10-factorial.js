#!/usr/bin/node
const a = parseInt(process.argv[2]);
if (isNaN(a)) {
  console.log(1);
} else {
  function factorial (a) {
    if (a === 0) {
      return 1;
    } else {
      return a * factorial(a - 1);
    }
  }
  console.log(factorial(a));
}
