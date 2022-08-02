#!/usr/bin/node
exports.esrever = function (list) {
  const myList = [];
  list.forEach(function (i) {
    myList.unshift(i);
  });
  return (myList);
};
