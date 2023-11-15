#!/usr/bin/node
const list = require('./100-data').list;
const mylist = list.map((item, index) => item * index);
console.log(list);
console.log(mylist);
