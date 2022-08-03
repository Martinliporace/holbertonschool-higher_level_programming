#!/usr/bin/node
const myDict = require('./101-data').dict;
const newDict = {};
for (const key in myDict) {
  if (myDict[key] in newDict) {
    newDict[myDict[key]].push(key);
  } else {
    newDict[myDict[key]] = [key];
  }
}
console.log(newDict);
