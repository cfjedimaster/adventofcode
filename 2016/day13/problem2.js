var PF = require('pathfinding');

let maxY = 50;
let maxX = 50;
const MGR_FAV = 1362;


let cells = [];

for(let x=0;x<maxX;x++) {
    cells[x] = [];
    for(let y=0;y<maxY;y++) {
        let thing = getThing(x,y);
        cells[x][y] = thing;
    }
}

//renderMaze(cells);

var pfgrid = new PF.Grid(maxX, maxY);
for(let x=0;x<cells.length;x++) {
    for(let y=0;y<cells[x].length;y++) {
        let v = cells[x][y];
        let walkable = (v == ".");
        pfgrid.setWalkableAt(x,y,walkable);
    }
}
var finder = new PF.AStarFinder();
var found = 0;
for(let x=0;x<maxX;x++) {
    for(let y=0;y<maxY;y++) {
        var gridBackup = pfgrid.clone();
        //good place?
        if(cells[x][y] == ".") {
            var path = finder.findPath(1, 1, x, y, gridBackup);
            if(path.length) {
                var steps = path.length - 1;
                if(steps <= 50) found++;
            }
        }
    }
}
//1242 is too high
console.log('found',found);
/*
Horrible name, but this returns wall/empty space

Find x*x + 3*x + 2*x*y + y + y*y.
Add the office designer's favorite number (your puzzle input).
Find the binary representation of that sum; count the number of bits that are 1.
If the number of bits that are 1 is even, it's an open space.
If the number of bits that are 1 is odd, it's a wall.
*/
function getThing(x,y) {
//    console.log(x,y);
    let initialResult = (x*x) + (3*x) + (2*x*y) + y + (y*y);
    initialResult += MGR_FAV;
    //http://stackoverflow.com/a/16155417/52160
    let binaryVersion = (initialResult >>> 0).toString(2);
    let bitCount = 0;
    for(let i=0;i<binaryVersion.length;i++) {
        let char = binaryVersion.substr(i,1);
        if(char === "1") bitCount++;
    }
    if(bitCount % 2 === 0) return ".";
    return "#";
}

function renderMaze(cells) {
    /*
    for(let x=0;x<cells.length;x++) {
        for(let y=0;y<cells[x].length;y++) {
            process.stdout.write(cells[x][y]);
        }
        process.stdout.write('\n');
    }
    */
    for(let y=0;y<cells[0].length;y++) {
        for(let x=0;x<cells[y].length;x++) {
            process.stdout.write(cells[x][y]);
        }
        process.stdout.write('\n');        
    }
}
