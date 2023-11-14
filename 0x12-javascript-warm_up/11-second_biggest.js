#!/usr/bin/node
let biggestint = 0, idx, mylist = [];

for (idx = 2; idx < process.argv.length; idx++) {
  if (Number.isNaN(parseInt(process.argv[idx])) === false) {
    mylist[idx - 2] = parseInt(process.argv[idx]);
  }
}

if (mylist.length > 1) {
  biggestint = Math.max.apply(null, mylist);
  idx = mylist.indexOf(biggestint);
  mylist[idx] = -Infinity;
  biggestint = Math.max.apply(null, mylist);
}

console.log(biggestint);
