#!/usr/bin/node
let nbItem = 0; // number of items to print
exports.logMe = function (item) {
  console.log(nbItem + ': ' + item);
  nbItem++;
};
