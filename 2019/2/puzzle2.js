const fs = require('fs');

function runCode(instructions, noun, verb) {
	let code = instructions.split(',').map(i => parseInt(i, 10));

	// Ray read damnit: To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2.
	code[1] = noun;
	code[2] = verb;

	let pos = 0;
	let ended = false;
	while(!ended) {
		let opcode = code[pos];

		if(opcode === 1) {
			//console.log('do addition');
			let p1 = code[pos+1];
			let p2 = code[pos+2];
			let target = code[pos+3];
			let sum = code[p1] + code[p2];
			code[target] = sum;
			//console.log(`I was told to get position ${p1} and ${p2} with values ${code[p1]} and ${code[p2]} for a sum of ${sum} and set it to ${target}`);
			pos+=4;

		}

		if(opcode === 2) {
			//console.log('do multiplication');
			let p1 = code[pos+1];
			let p2 = code[pos+2];
			let target = code[pos+3];
			let product = code[p1] * code[p2];
			code[target] = product;
			pos+=4;
		}

		if(opcode === 99) {
			//console.log('ending');
			ended = true;
		}

		if(pos+1 >= code.length) ended=true;
	}
	return code;
}


input = fs.readFileSync('./input.txt', 'utf8').trim();
// BRUTE FORCE FTW!
let target = 19690720;
for(let noun=0;noun < 100; noun++) {
	for(let verb=0;verb < 100; verb++) {
		let result = runCode(input, noun, verb)[0];
		if(result === target) {
			console.log('Success: '+noun, verb);
			console.log('Answer: '+(noun*100 + verb));
		}
	}
}
//console.log(runCode(input,12,2)[0]);