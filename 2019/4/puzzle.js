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
	let double = s.match(/([0-9])\1/);
	if(!double) return false;
	//console.log(`${x} has a double`);
	let last = -1;
	for(let i=0;i<s.length;i++) {
		let c = s.charAt(i);
		let thisNum = parseInt(c, 10);
		if(thisNum < last) return false;
		last = thisNum;
	}
	return true;
}

console.log(`Valid passwords: ${passwordCount}`);