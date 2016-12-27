
let initTime = 2;
let time = initTime;

//let input = `Disc #1 has 5 positions; at time=0, it is at position 4.
//Disc #2 has 2 positions; at time=0, it is at position 1.`;
let input = `Disc #1 has 5 positions; at time=0, it is at position 2.
Disc #2 has 13 positions; at time=0, it is at position 7.
Disc #3 has 17 positions; at time=0, it is at position 10.
Disc #4 has 3 positions; at time=0, it is at position 2.
Disc #5 has 19 positions; at time=0, it is at position 9.
Disc #6 has 7 positions; at time=0, it is at position 0.`;

let discs = [];
let capsule = 0;

input.split('\n').forEach(function(i) {
	let parts = i.split(' ');
	let numpos = Number(parts[3]);
	let inipos = Number(parts[11].substr(0, parts[11].length-1));
	discs.push({name:parts[1], numpos:numpos, inipos:inipos, pos:inipos});
});


//do initial moves
for(x=0;x<initTime;x++) { moveDiscs(); }

function moveDiscs() {
	discs.forEach(function(disc) {
		disc.pos++;
		if(disc.pos == disc.numpos) disc.pos = 0;
		console.log('Disc '+disc.name+' is at position '+disc.pos);
	});
}


console.log(discs);

done = false; sanity = 0;
while(!done) {
	time++;
	moveDiscs();
	console.log('At time '+time+' the capsule is at '+capsule);
	//move the discs
	if(discs[capsule].pos === 0) {
		console.log('i can fall');
		capsule++;
		if(capsule === discs.length) {
			done = true;
			console.log('Success for time '+initTime);
		}
	} else {
		done = true;
		console.log('Failure for time '+initTime);
	}
	sanity++; if(sanity>2) { done = true; };
}