#!/usr/bin/node

const n = parseInt(process.argv[2]);
if (n === NaN)
    console.log('Not a number');
else
    console.log(n);
