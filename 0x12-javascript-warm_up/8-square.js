#!/usr/bin/node

const n = parseInt(process.argv[2]);

if (!isNaN(n)) {
  let str = '';
  for (let i = 0; i < n; ++i) {
    for (let j = 0; j < n; ++j) {
      str += 'X';
    }
    str += '\n';
  }
  str = str.slice(0, str.length - 1);
  console.log(str);
} else {
  console.log('Missing size');
}
