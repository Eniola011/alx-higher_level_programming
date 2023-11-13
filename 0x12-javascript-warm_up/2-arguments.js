#!/usr/bin/node
const argmt = process.argv.length;

if (argmt <= 2) {
  console.log('No argument');
} else if (argmt === 3) {
  console.log('Agrument found');
} else {
  console.log('Argument found');
}
