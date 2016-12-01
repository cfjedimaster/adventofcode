var fs = require('fs');
var input = fs.readFileSync('./input.txt','utf8');
//var input = 'R2, R2, R2';
var steps = input.split(', ');

/*
we start at 1,1
loop over each step and figure out the new pos
*/
var currentPos = [1,1];
var currentDir = "N";  // North

steps.forEach((step) => {
    var dir = step.substring(0,1);
    var dis = Number(step.substring(1));
    console.log(dir+','+dis);

    console.log('current direction '+currentDir);
    if(dir === "R") turnRight();
    if(dir === "L") turnLeft();
    console.log('new direction '+currentDir);
    console.log('current pos '+currentPos);
    move(dis);
    console.log('new pos '+currentPos);
});

var distance = Math.abs(1-currentPos[0]) + Math.abs(1-currentPos[1]);
console.log('Distance is '+distance);

function move(x) {
    /*
    given a direction and current pos, um, move
    */
    if(currentDir === "N") currentPos = [currentPos[0] + x, currentPos[1]];
    if(currentDir === "E") currentPos = [currentPos[0], currentPos[1] + x];
    if(currentDir === "S") currentPos = [currentPos[0] - x, currentPos[1]];
    if(currentDir === "W") currentPos = [currentPos[0], currentPos[1] - x];

}

function turnRight() {
    switch(currentDir) {
        case "N": {
            currentDir = "E";
            break;
        }
        case "E": {
            currentDir = "S";
            break;
        }
        case "S": {
            currentDir = "W";
            break;
        }
        case "W": {
            currentDir = "N";
            break;
        }
    }
}

function turnLeft() {
    switch(currentDir) {
        case "N": {
            currentDir = "W";
            break;
        }
        case "E": {
            currentDir = "N";
            break;
        }
        case "S": {
            currentDir = "E";
            break;
        }
        case "W": {
            currentDir = "S";
            break;
        }
    }
}