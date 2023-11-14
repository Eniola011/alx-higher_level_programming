#!/usr/bin/node
const Rectangle = require('./4-rectangle');
// A square and inherits from Rectangle of 4-rectangle.js
class Square extends Rectangle {
  constructor (size) { // The constructor must take 1 argument: size
    super(size, size); // The constructor of Rectangle must be called (by using super())
  }
}

module.exports = Square;
