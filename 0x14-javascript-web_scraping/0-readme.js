#!/usr/bin/node
// Write a script that reads and prints the content of a file.
const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (data === undefined) {
    console.log(err);
  } else {
    console.log(data);
  }
});
