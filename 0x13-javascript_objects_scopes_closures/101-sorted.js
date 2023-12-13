#!/usr/bin/node
// Rectangle class

const dict = require('./101-data').dict;
const array = Object.entries(dict);
const newFormat = {};

for (const [key, value] of array) {
  if (newFormat[value] === undefined) {
    newFormat[value] = [];
  }
  newFormat[value].push(key);
}
console.log(newFormat);
