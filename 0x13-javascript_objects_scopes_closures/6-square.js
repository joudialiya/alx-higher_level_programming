#!/usr/bin/node
// Rectangle class
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    let str = '';
    for (let i = 0; i < this.height; ++i) {
      for (let j = 0; j < this.width; ++j) {
        str += c;
      }
      str += '\n';
    }
    console.log(str.slice(0, str.length - 1));
  }
}

module.exports = Square;
