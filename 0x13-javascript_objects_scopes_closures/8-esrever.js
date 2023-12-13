#!/usr/bin/node
// Rectangle class

exports.esrever = function (list) {
  const cpy = [];
  for (let i = 0; i < list.length; ++i) {
    cpy.push(list[list.length - 1 - i]);
  }
  return cpy;
};
