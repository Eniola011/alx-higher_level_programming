#!/usr/bin/node
const argmt = parseInt(process.argv[2]);
if (Number.isNaN(argmt)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + argmt);
}
