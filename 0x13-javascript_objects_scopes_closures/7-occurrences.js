#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nbOccurence = 0;
  for (let idx = 0; idx < list.length; idx++) {
    if (searchElement === list[idx]) {
      nbOccurence++;
    }
  }
  return nbOccurence;
};
