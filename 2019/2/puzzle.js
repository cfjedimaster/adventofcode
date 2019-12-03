const fs = require('fs');

function runCode(instructions) {
	let code = instructions.split(',').map(i => parseInt(i, 10));

	// Ray read damnit: To do this, before running the program, replace position 1 with the value 12 and replace position 2 with the value 2.
	code[1] = 12;
	code[2] = 2;

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
			console.log('ending');
			ended = true;
		}

		if(pos+1 >= code.length) ended=true;
	}
	return code;
}

//test inputs

// this one should return "2,0,0,0,99"
input = "1,0,0,0,99";
//console.log(runCode(input));

// this one should return "2,3,0,6,99:
input = "2,3,0,3,99";
//console.log(runCode(input));

// this one should return 2,4,4,5,99,9801
input = "2,4,4,5,99,0";
//console.log(runCode(input));

// this one should return 30,1,1,4,2,5,6,0,99
input = "1,1,1,4,99,5,6,0,99";
//console.log(runCode(input));

// 466644 is too low
input = fs.readFileSync('./input.txt', 'utf8').trim();
console.log(runCode(input)[0]);