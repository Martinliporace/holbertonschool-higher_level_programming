#!/usr/bin/node
let count = 0;
exports.logMe = function (item) {
  const out = console.log(count + ': ' + item);
  count++;
  return (out);
};
