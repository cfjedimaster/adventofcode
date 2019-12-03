const fs = require('fs');

let contents = fs.readFileSync('./input.txt', 'utf8').trim().split('\n');

function fuel(mass) {
	let toAdd = Math.floor(mass/3) - 2;
	//console.log('toAdd is '+toAdd);
	let result = toAdd;
	while(toAdd > 0) {
		toAdd = Math.floor(toAdd/3) - 2;
		//console.log('in loop', toAdd);
		if(toAdd > 0) result += toAdd;
	}	
	return result;
}

// test inputs
/*
console.log(fuel(14));
console.log(fuel(1969));
console.log(fuel(100756));
*/

let sum = 0;
contents.forEach(c => {
	c = parseInt(c, 10);
	sum += fuel(c);
	//console.log((++counter)+' Sum is now '+sum+ ' and c was '+c+' and fuel was '+fuel(c));
});
console.log(sum);
