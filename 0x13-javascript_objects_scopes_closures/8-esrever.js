#!/usr/bin/node
exports.esrever = function (list) {
  const revList = []; // reversed list
  let item = 0; // item in a list
  for (let idx = list.length - 1; idx >= 0; idx--) {
    revList[idx] = list[item]; // add item to reversed list
    item++;
  }
  return revList;
};
