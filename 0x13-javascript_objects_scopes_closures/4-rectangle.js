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
      str += '\n';
    }
    console.log(str.slice(0, str.length - 1));
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }

  rotate () {
    this.width, this.height = this.height, this.width;
  }
}

module.exports = Rectangle;
