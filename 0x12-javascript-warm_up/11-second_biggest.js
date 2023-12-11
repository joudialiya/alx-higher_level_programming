#!/usr/bin/node

const nums = [];

for (let i = 2; i < process.argv.length; ++i) {
  nums.push(parseInt(process.argv[i]));
}
if (nums.length < 2) {
  console.log('0');
} else {
  console.log(`${Math.max(...nums)}`);
}
