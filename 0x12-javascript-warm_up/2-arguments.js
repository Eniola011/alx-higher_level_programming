#!/usr/bin/node
const argmt = process.argv.length - 2;
if (argmt === 0) {
  console.log('No argument');
} else if (argmt === 1) {
  console.log('Agrument found');
} else {
  console.log('Arguments found');
}
