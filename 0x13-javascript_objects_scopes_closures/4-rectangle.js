#!/usr/bin/node
// Create an instance method called rotate() that exchanges the width and the height of the rectangle
// Create an instance method called double() that multiples the width and the height of the rectangle by 2
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    // prints the rectangle using the character X
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    // exchange values
    const tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    // multiplies rectangle by 2
    this.width *= 2;
    this.heigth *= 2;
  }
}

module.exports = Rectangle;
