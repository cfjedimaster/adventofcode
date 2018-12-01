const fs = require('fs');

let steps = fs.readFileSync('./input.txt', 'UTF8').split('\n');
//let steps = '+7, +7, -2, -7, -4'.split(' ');


let freqs = {};

let start = 0;
let pos = 0;
while(true) {
	//console.log(`start=${start} step=${s}`)
	s = steps[pos].trim();
	pos++;
	if(pos === steps.length) {
		pos=0;
	}

	if(!s.length) continue;
	start += parseInt(s,10);
	if(!freqs[start]) {
		freqs[start] = 1;
	} else {
		// second time
		console.log('Winner is '+start);
		process.exit(1);
	}
}

