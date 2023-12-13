#!/usr/bin/node
// Rectangle class

exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const e of list) {
    if (e === searchElement) {
      count += 1;
    }
  }
  return count;
};
