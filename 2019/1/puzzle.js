const fs = require('fs');

let contents = fs.readFileSync('./input.txt', 'utf8').trim().split('\n');

function fuel(mass) {
	return Math.floor(mass/3) - 2;
}

/* test inputs
console.log(fuel(12));
console.log(fuel(14));
console.log(fuel(1969));
console.log(fuel(100756));
*/

let sum = 0;
contents.forEach(c => {
	c = parseInt(c, 10);
	sum += fuel(c);
});
// 3296267 is too low
console.log(sum);