#!/usr/bin/node

function fact (a) {
  if (a === 0 || isNaN(a)) {
    return 1;
  }
  return a * fact(a - 1);
}

console.log(`${fact(parseInt(process.argv[2]))}`);
