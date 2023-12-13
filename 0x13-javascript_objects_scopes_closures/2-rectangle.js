#!/usr/bin/node
// Rectangle class

module.exports = class Rectangle {
  constructor (w = 0, h = 0) {
    if (w >= 0 && h >= 0) {
      this.width = w;
      this.height = h;
    }
  }
};
