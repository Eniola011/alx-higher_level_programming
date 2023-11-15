#!/usr/bin/node
const fs = require('fs');

const argmt1 = fs.readFileSync(process.argv[2]).toString();
const argmt2 = fs.readFileSync(process.argv[3]).toString();

fs.writeFileSync(process.argv[4], argmt1 + argmt2);
