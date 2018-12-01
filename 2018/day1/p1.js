//let input = '-1, -2, -3';
const fs = require('fs');

let steps = fs.readFileSync('./input.txt', 'UTF8').split('\n');

let start = 0;

steps.forEach(s => {
	//console.log(`start=${start} step=${s}`)
	s = s.trim();
	if(s.length) start += parseInt(s,10);
});

console.log(start);