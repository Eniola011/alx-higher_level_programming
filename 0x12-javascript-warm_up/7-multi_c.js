#!/usr/bin/node
const argmt1 = parseInt(process.argv[2]);
if (!isNaN(argmt1)) {
  for (let idx = 0; idx < argmt1; idx++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
