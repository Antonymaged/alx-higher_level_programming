#!/usr/bin/node
if (process.argv === undefined || isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number:', parseInt(process.argv[2]));
}
