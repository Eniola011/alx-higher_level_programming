#!/usr/bin/node
const argmt = process.argv;
if (argmt[2] === 0) {
  console.log('No argument');
} else if (argmt[3] === 0) {
  console.log('Agrument found');
} else {
  console.log('Arguments found');
}
