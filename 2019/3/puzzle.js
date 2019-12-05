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

/*
let wires = [
	'R8,U5,L5,D3',
	'U7,R6,D4,L4'
];
*/

let wires = fs.readFileSync('./input.txt', 'utf8').trim().split('\n');

//let wires = ['R75,D30,R83,U83,L12,D49,R71,U7,L72','U62,R66,U55,R34,D71,R55,D58,R83'];
//135
//let wires = ['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51','U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'];
console.log(`total wires? ${wires.length}`);
wires.forEach(w => {
	let path = w.split(',');
	let pos = { x: 0, y: 0 };
	path.forEach(p => {
		let dir = p.charAt(0);
		let len = parseInt(p.slice(1),10);
		console.log('go in dir '+dir+' for '+len);
		if(dir === 'U') {
			for(let i=0;i<len;i++) {
				pos.y++;
				if(!grid[pos.x]) grid[pos.x] = [];
				if(grid[pos.x][pos.y] && grid[pos.x][pos.y] === 1) intersections.push({x:pos.x, y:pos.y});
				grid[pos.x][pos.y] = 1;		
			}
		} else if(dir === 'D') {
			for(let i=0;i<len;i++) {
				pos.y--;
				if(!grid[pos.x]) grid[pos.x] = [];
				if(grid[pos.x][pos.y] && grid[pos.x][pos.y] === 1) intersections.push({x:pos.x, y:pos.y});
				grid[pos.x][pos.y] = 1;		
			}
		} else if (dir === 'L') {
			for(let i=0;i<len;i++) {
				pos.x--;
				if(!grid[pos.x]) grid[pos.x] = [];
				if(grid[pos.x][pos.y] && grid[pos.x][pos.y] === 1) intersections.push({x:pos.x, y:pos.y});
				grid[pos.x][pos.y] = 1;		
			}
		} else if(dir === 'R') {
			for(let i=0;i<len;i++) {
				pos.x++;
				if(!grid[pos.x]) grid[pos.x] = [];
				if(grid[pos.x][pos.y] && grid[pos.x][pos.y] === 1) intersections.push({x:pos.x, y:pos.y});
				grid[pos.x][pos.y] = 1;		
			}

		}
		// save to grid
		if(!grid[pos.x]) grid[pos.x] = [];
		grid[pos.x][pos.y] = 1;
		//console.log('at '+JSON.stringify(pos));
	});
});

//draw(grid);
let min = Number.MAX_SAFE_INTEGER;
intersections.forEach(i => {
	let distance = Math.abs(i.x) + Math.abs(i.y);
	console.log('for '+JSON.stringify(i) + ' the distance is '+distance);
	if(distance < min) min = distance;
});

console.log(min);