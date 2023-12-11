#!/usr/bin/node

exports.callMeMoby = function (n, callback) {
  for (let i = 0; i < n; ++i){
    callback();
  }
};
