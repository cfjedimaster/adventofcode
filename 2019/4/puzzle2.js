const input = '172930-683082';

let [min,max] = input.split('-');
min = parseInt(min, 10); 
max = parseInt(max, 10);
//min = 1; max=20;
console.log(`Ranging from ${min} to ${max}`);
let passwordCount = 0;

for(let i=min; i<=max; i++) {
	if(validPassword(i)) passwordCount++;
}

function validPassword(x) {
	let s = new String(x);

	let last = -1;
	for(let i=0;i<s.length;i++) {
		let c = s.charAt(i);
		let thisNum = parseInt(c, 10);
		if(thisNum < last) return false;
		last = thisNum;
	}

	let double = s.matchAll(/([0-9])\1/g);

	for(const match of double) {
		//check double.index to see if index-1 is the same
		let matchNum = match[0].charAt(0);
//console.log('matchNum', matchNum, ' index', match.index);
		if(
			(
				match.index === 0 || s.charAt(match.index-1) !== matchNum
			) &&
			(
				match.index === s.length-1 || s.charAt(match.index+2) !== matchNum
			)
		) return true;
	}
	return false;
}
//758 is too low, 1619 is too high, 1493 is too high
console.log(`Valid passwords: ${passwordCount}`);