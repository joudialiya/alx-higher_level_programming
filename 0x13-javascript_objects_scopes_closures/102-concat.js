#!/usr/bin/node
const fs = require('node:fs');
try {
  fs.writeFileSync(
    process.argv[4],
    fs.readFileSync(process.argv[2]) + '\n'
    fs.readFileSync(process.argv[3])
  );
} catch (e) {
  console.log(e);
}
