#!/usr/bin/node

exports.addMeMaybe = function (n, callback) {
  n += 1;
  callback(n);
};
