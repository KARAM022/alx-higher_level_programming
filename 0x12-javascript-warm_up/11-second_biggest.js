#!/usr/bin/node

function secondBiggest (arr) {
  if (arr.length <= 1) {
    return 0;
  } else {
    const integers = arr.map(arg => parseInt(arg)).sort((a, b) => a - b);
    const uniqueIntegers = [...new Set(integers)];
    if (uniqueIntegers.length >= 2) {
      return uniqueIntegers[uniqueIntegers.length - 2];
    } else {
      return 0;
    }
  }
}

const args = process.argv.slice(2);
console.log(secondBiggest(args));
