#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const current in list) {
    if (list[current] === searchElement) {
      count++;
    }
  }
  return count;
};
