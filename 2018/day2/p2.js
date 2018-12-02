/*
let input = `abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz`.split('\n');
*/
const fs = require('fs');

let input = fs.readFileSync('./input.txt', 'UTF8').split('\n');


for(let x=0;x<input.length;x++) {
	for(let y=0;y<input.length;y++) {
		//I should not compare the same, but since they won't be a match, it won't matter
		let closeResult = closeString(input[x], input[y]);
		if(closeResult > 0) {
			//console.log(input[x]);
			//console.log(input[y]);
			// there's some weird bug where the console msg below doesn't print right. Never figured it out.
			console.log(`Match with ${input[x]} and ${input[y]}`);
			console.log('Match with '+input[x]+' and '+input[y]);
			//console.log(`it matched at ${closeResult}`);
			let chars = input[x].split('');
			chars.splice(closeResult, 1);
			let result = chars.join('');
			console.log('Result='+result);
			process.exit(1);
		}
	}
}

/*
I return 0 if the strings do not differ by exactly ONE char in the same place.
I return X which is the position of the ONE char diff
*/
function closeString(a, b) {
	let differences = 0;
	let match = 0;
	for(let x=0;x<a.length;x++) {
		let c1 = a.charAt(x);
		let c2 = b.charAt(x);
		if(c1 !== c2) {
			differences++;
			match = x;
			if(differences > 1) return 0;
		}
	}

	return match;
}