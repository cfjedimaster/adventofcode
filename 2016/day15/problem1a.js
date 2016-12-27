let initTime = 0;

let input2 = `Disc #1 has 5 positions; at time=0, it is at position 4.
//Disc #2 has 2 positions; at time=0, it is at position 1.`;
let input = `Disc #1 has 5 positions; at time=0, it is at position 2.
Disc #2 has 13 positions; at time=0, it is at position 7.
Disc #3 has 17 positions; at time=0, it is at position 10.
Disc #4 has 3 positions; at time=0, it is at position 2.
Disc #5 has 19 positions; at time=0, it is at position 9.
Disc #6 has 7 positions; at time=0, it is at position 0.`;

function initDiscs(s) {
	let discs = [];

	s.split('\n').forEach(function(i) {
		let parts = i.split(' ');
		let numpos = Number(parts[3]);
		let inipos = Number(parts[11].substr(0, parts[11].length-1));
		discs.push({name:parts[1], numpos:numpos, inipos:inipos, pos:inipos});
	});

	return discs;

}

function moveDiscs(d) {
	d.forEach(function(disc) {
		disc.pos++;
		if(disc.pos == disc.numpos) disc.pos = 0;
		//console.log('Disc '+disc.name+' is at position '+disc.pos);
	});
	return d;
}


sanity = 0;
while(1) {

	discs = initDiscs(input);

	//do initial moves
	for(x=0;x<initTime;x++) { discs = moveDiscs(discs); }
	time = initTime++;
//	console.log('TESTING TIME '+time);
	if(time % 10000 === 0) process.stdout.write('#');
	let capsule = 0;

	done = false; 

	while(!done) {
		time++;
		discs = moveDiscs(discs);
//		console.log('At time '+time+' the capsule is at '+capsule);

		//move the discs
		if(discs[capsule].pos === 0) {
//			console.log('i can fall');
			capsule++;
			if(capsule === discs.length) {
				done = true;
				console.log('\nSuccess for time '+(initTime-1));
				process.exit();
			}
		} else {
			done = true;
//			console.log('Failure for time '+(initTime-1));
		}

		sanity++;
		//if(sanity > 3) process.exit();
	}


}

//right answer was 148737