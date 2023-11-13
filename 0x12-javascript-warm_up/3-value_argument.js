#!/usr/bin/node
const argmt = process.argv[2];
if (argmt === undefined) {
  console.log('No argument');
} else {
  console.log(argmt);
}
