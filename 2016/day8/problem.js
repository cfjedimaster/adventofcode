
//screen size
let width = 50;
let height = 6;
let screen = seedScreen(width,height);

renderScreen(screen, width, height);
/*
let input = 'rect 3x2';
screen = parseInput(screen, input);
renderScreen(screen, width, height);

console.log('NOW DO COL');
screen = parseInput(screen, 'rotate column x=1 by 1');
renderScreen(screen, width, height);

console.log('NOW DO RECT');

screen = parseInput(screen, 'rotate row y=0 by 4');
renderScreen(screen, width, height);

console.log('NOW DO COL');
screen = parseInput(screen, 'rotate column x=1 by 1');
renderScreen(screen, width, height);
*/

const fs = require('fs');
const input = fs.readFileSync('./input.txt','utf8');

let good = 0;
let lines = input.split('\n');
lines.forEach(function(line) {
	screen = parseInput(screen, line);
	renderScreen(screen, width, height);
});

let total = getTotal(screen);
console.log(total);

function getTotal(s) {
	let total = 0;
	for(let x=0;x<s.length;x++) {
		for(let y=0;y<s[x].length;y++) {
			if(s[x][y] === "#") total++;
		}
	}
	return total;
}

function parseInput(screen, i) {
	if(i.indexOf('rect') === 0) {
		let dim = i.split(' ')[1];
		let width = dim.split('x')[0];
		let height = dim.split('x')[1];
		return drawRect(screen, width, height);
	}

	//	rotate row y=A by B
	if(i.indexOf('rotate row') === 0) {
		let dim = i.split(' row y=')[1];
		let row = Number(dim.split(' by ')[0]);
		let offset = Number(dim.split(' by ')[1]);
		return rotateRow(screen, width, height, row, offset);
	}

	//	otate column x=1 by 1
	if(i.indexOf('rotate column') === 0) {
		let dim = i.split(' column x=')[1];
		let col = Number(dim.split(' by ')[0]);
		let offset = Number(dim.split(' by ')[1]);
		return rotateColumn(screen, width, height, col, offset);
	}

	throw('Unknown command: '+i);
}

function rotateColumn(s, w, h, c, o) {
	//##.  => .## (1)
	//##. => #.# (2)
	let originalCol = s[c];
//	console.log('offset is '+o);
//	console.log('origCol='+originalCol.join(''));
	let newCol = [];
	for(let x=0;x<originalCol.length;x++) {
		let thisVal = originalCol[x];
		let newPos = x + o;
//		console.log('thisVal='+thisVal+' newPos='+newPos);
		if(newPos >= originalCol.length) newPos =  newPos - originalCol.length;
//		console.log(' newPos='+newPos);
		newCol[newPos] = thisVal;
	}
//	console.log('newCol='+newCol);
	s[c] = newCol;
	return s;
}

function rotateRow(s, w, h, r, o) {
	/*
	so given ##00# and offset of 2, 
	we make a new list starting at 2. 
	#00##
	*/
	let originalRow = [];
    for(let x=0;x<w;x++) {
        for(let i=0;i<h;i++) {
			if(i === r) {
				originalRow.push(s[x][i]);
			}
        }
    }
//	console.log('or: '+originalRow.join('')+'-');
	let newRow = [];
	let done = 0;
	//because:
	o++;
	for(let x = o; x < o+originalRow.length; x++) {
		let pos = x;
//		console.log('trying to set '+pos);
		if(pos > w) pos = pos-w;
//		console.log('really '+pos);
//		newRow.push(originalRow[x]);
//console.log('val to set is '+originalRow[done]);
		newRow[pos-1] = originalRow[done];
		done++;
//		console.log('new Row len is now '+newRow.length);
	}
//	console.log('newRow: '+newRow.join(''));
    for(let x=0;x<w;x++) {
        for(let i=0;i<h;i++) {
			if(i === r) {
				s[x][i] = newRow[x];
			}
        }
    }

	return s;
	
}

function drawRect(s,w,h) {
	console.log('going to draw '+w+','+h);
	for(let i=0;i<w;i++) {
		for(let x=0;x<h;x++) {
			s[i][x] = "#";
		} 
	}
	return s;
}

function seedScreen(w,h) {
    let screen = [];
    for(let i=0;i<w;i++) {
        for(let x=0;x<h;x++) {
            //console.log('setting s['+i+']['+x+']');
            if(!screen[i]) screen[i] = [];
            screen[i][x] = ".";
        }
    }
    return screen;
}

function renderScreen(s,width,height) {
    var result = '';
    for(let x=0;x<height;x++) {
        for(let i=0;i<width;i++) {
            result += s[i][x];
        }
        result += '\n';
    }
    console.log(result);
}