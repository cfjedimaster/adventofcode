/*
let input = `abcdef
bababc
abbcde
abcccd
aabcdd
abcdee
ababab`.split('\n');
*/
const fs = require('fs');

let input = fs.readFileSync('./input.txt', 'UTF8').split('\n');

// how many IDs have 2 matching letters
let totalTwo = 0;
// ditto for three
let totalThree = 0;

input.forEach(i => {
	console.log(i, hasTwo(i), hasThree(i));
	if(hasExactly(i,2)) totalTwo++;
	if(hasExactly(i,3)) totalThree++
});

let checkSum = totalTwo * totalThree;
console.log(checkSum);

function hasExactly(s, x) {
	for(let i=97;i<=122;i++) {
		let letter = String.fromCharCode(i);
		let reg = RegExp(letter, 'g');
		let count = (s.match(reg) || []).length;
		//console.log('for s='+s+' the count of '+letter+ ' is '+count);
		if(count === x) return true;
	}
	return false;
}

// I know these could be done in regex much slicker.
// my initial implementation below
function hasTwo(s) {
	for(let i=97;i<=122;i++) {
		let letter = String.fromCharCode(i);
		let reg = RegExp(letter, 'g');
		let count = (s.match(reg) || []).length;
		//console.log('for s='+s+' the count of '+letter+ ' is '+count);
		if(count === 2) return true;
	}
	return false;
}

function hasThree(s) {
	for(let i=97;i<=122;i++) {
		let letter = String.fromCharCode(i);
		let reg = RegExp(letter, 'g');
		let count = (s.match(reg) || []).length;
		//console.log('for s='+s+' the count of '+letter+ ' is '+count);
		if(count === 3) return true;
	}
	return false;
}