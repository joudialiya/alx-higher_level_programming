#!/usr/bin/node

let nums = [];

for (let i = 2; i < process.argv.length; ++i) {
  nums.push(parseInt(process.argv[i]));
}
nums.sort();

if (nums.length < 2) {
  console.log('0');
} else {
  console.log(`${nums[nums.length - 2]}`);
}
