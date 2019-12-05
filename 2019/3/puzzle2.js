const fs = require('fs');

function draw(g) {
	// assume some max
	for(let i=0; i<10; i++) {
		for(let j=0; j<10; j++) {
			if(grid[i] && grid[i][j]) process.stdout.write('X');
			else process.stdout.write('.');
		}
		process.stdout.write('\n');
	}
}


/*
store a list of every place visited, 
as you draw a wire, if you have already visited X, Y, add to list of intersections
then just find the closest
*/
let grid = [];
let intersections = [];

let wires = fs.readFileSync('./input.txt', 'utf8').trim().split('\n');

//let wires = ['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83'];
//135
//let wires = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'];

//let wires = ['R8,U5,L5,D3','U7,R6,D4,L4'];

wires.forEach((w,index) => {
	let path = w.split(',');
	let pos = { x: 0, y: 0 };
	
	let steps = 0;
	path.forEach(p => {
		let dir = p.charAt(0);
		let len = parseInt(p.slice(1),10);

		if(dir === 'U') {
			toMove = 'y';
			toMoveDir = 1;
		} else if(dir === 'D') {
			toMove = 'y';
			toMoveDir = -1;
		} else if(dir === 'L') {
			toMove = 'x';
			toMoveDir = -1;
		} else {
			toMove = 'x';
			toMoveDir = 1;
		}

		for(let i=0;i<len;i++) {
			steps++;

			pos[toMove] += toMoveDir;
			if(!grid[pos.x]) grid[pos.x] = [];

			if(grid[pos.x][pos.y] && index === 1) {
				// only log the intersection if this is the first time
				let hasOne = intersections.filter(i => {
					return i.x == pos.x && i.y == pos.y;
				});
//				console.log(`existing int for ${pos.x},${pos.y}? ${hasOne}`);
				if(hasOne.length === 0) {
					intersections.push({x:pos.x, y:pos.y, steps:steps+grid[pos.x][pos.y]});
				}
			}
			// i only record steps on wire1, cuz for wire 2, we only care about intersections
			// and i only record my first visit
			if(index === 0 && !grid[pos.x][pos.y]) grid[pos.x][pos.y] = steps;		
		}

		// save to grid
		/*
		if(!grid[pos.x]) grid[pos.x] = [];
		grid[pos.x][pos.y] = 1;
		*/
		//console.log('at '+JSON.stringify(pos));
	});
});
draw(grid);
let min = Number.MAX_SAFE_INTEGER;
intersections.forEach(i => {
	if(i.steps < min) min = i.steps;
});

// 9007199254740991 is too high, of course, 19 is wrong, 2 is wrong
console.log(min);