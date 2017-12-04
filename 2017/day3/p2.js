/*
so given an initial position for 1 at (1,1), we know 2 is (2,1), we can
then begin counting up and around to the left.
*/

let grid = [ [], [] ];

grid[1] = [];
grid[1][1] = 1;
grid[2] = [];
grid[2][1] = 1;

// our final position
let target = 999;
//current direction, since we start with 2, it is north
let direction = 'N';
// current position
let position = [2,1];

for(let i=3; i<=target; i++) {
    console.log('doing '+i+ ' moving '+direction);

    if(direction === 'N') {
        position[1]++;
        grid[position[0]][position[1]] = getSum(position);
        // we turn left (W) if the position to our left is empty
        if(!grid[position[0]-1][position[1]]) direction='W';
    } else if(direction === 'W') {
        position[0]--;
        if(!grid[position[0]]) grid[position[0]] = [];
        grid[position[0]][position[1]] = getSum(position);
        // we turn left (S) if the position beneath us is empty
        if(!grid[position[0]][position[1]-1]) direction='S';        
    } else if(direction === 'S') {
        position[1]--;
        grid[position[0]][position[1]] = getSum(position);
        // we turn left (E) if position right is empty
        if(!grid[position[0]+1][position[1]]) direction='E';
    } else if(direction === 'E') {
        position[0]++;
        if(!grid[position[0]]) grid[position[0]] = [];
        grid[position[0]][position[1]] = getSum(position);
        // we turn left (N) if the position above us is empty
        if(!grid[position[0]][position[1]+1]) direction='N';        
    }
    
//    console.log('position='+position, 'direction='+direction);
}

// from wikipedia, |p1 - q1| + |p2 - q2|
let dist = Math.abs(1-position[0]) + Math.abs(1-position[1]);
console.log('dist='+dist);

// i check every position around me and get the total
function getSum(position) {
    console.log('getSum, '+position);
    let total = 0;
    // we will go N, NE, E, SE, S, SW, W, NW
    // N
    if(grid[position[0]][position[1]+1]) total += grid[position[0]][position[1]+1];
    //console.log('after N, '+total);
    // NE
    if(grid[position[0]+1] && grid[position[0]+1][position[1]+1]) total += grid[position[0]+1][position[1]+1];
    //console.log('after NE, '+total);
    // E
    if(grid[position[0]+1] && grid[position[0]+1][position[1]]) total += grid[position[0]+1][position[1]];
    //console.log('after E, '+total);
    // SE
    if(grid[position[0]+1] && grid[position[0]+1][position[1]-1]) total += grid[position[0]+1][position[1]-1];
    //console.log('after SE, '+total);
    // S
    if(grid[position[0]][position[1]-1]) total += grid[position[0]][position[1]-1];
    //console.log('after S, '+total);
    // SW
    if(grid[position[0]-1] && grid[position[0]-1][position[1]-1]) total += grid[position[0]-1][position[1]-1];
    //console.log('after SW, '+total);
    // W
    if(grid[position[0]-1] && grid[position[0]-1][position[1]]) total += grid[position[0]-1][position[1]];
    //console.log('after W, '+total);
    // NW
    if(grid[position[0]-1] && grid[position[0]-1][position[1]+1]) total += grid[position[0]-1][position[1]+1];
    //console.log('after NW, '+total);

    //console.log('returning total '+total);
    if(total > 289326) {
        console.log('winning total is '+total);
        process.exit(1);
    }
    return total;
}