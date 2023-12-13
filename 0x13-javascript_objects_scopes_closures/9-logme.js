#!/usr/bin/node
// Rectangle class
let index = 0;
exports.logMe = function (item) {
  console.log(`${index}: ${item}`);
  ++index;
};
