#!/usr/bin/node
// Rectangle class

class Square extends require('./5-square') {
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
