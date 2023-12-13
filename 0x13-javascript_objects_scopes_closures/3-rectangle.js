#!/usr/bin/node
// Rectangle class
class Rectangle {
  constructor (w = 0, h = 0) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let str = '';
    for (let i = 0; i < this.height; ++i) {
      for (let j = 0; j < this.width; ++j) {
        str += 'X';
      }
      str = '\n';
    }
    console.out(str);
  }
}

module.exports = Rectangle;
