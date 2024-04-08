#!/usr/bin/node

if (!process.argv[2]) {
  console.log('No argument');
} else {
  process.argv.forEach((val, index) => {
    if (index >= 2) {
      console.log(val);
    }
  })
}
