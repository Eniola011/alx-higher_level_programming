#!/usr/bin/node
const Rectangle = require('./5-square');
// A square and inherits from Rectangle of 4-rectangle.js

class Square extends Rectangle {
  charPrint (c) {
    // prints the rectangle using the character c
    if (c === undefined) { // If c is undefined, use the character X
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
