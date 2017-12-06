const fs = require('fs');
let inputs = fs.readFileSync('./input.txt', 'UTF8').split('\n');

// I could probably do this below
for(var i=0;i<inputs.length;i++) {
    inputs[i] = Number(inputs[i]);
}

let index = 0;
let steps = 0;

let inMaze = true;

let sanity = 0;

while(inMaze) {
    steps++;

    let thisJump = inputs[index];
    if((index + thisJump) >= inputs.length) {
        inMaze = false;
        console.log('Exit maze in '+steps+' steps.');
    } else {
        if(inputs[index] >= 3) inputs[index]--;
        else inputs[index]++;
        index = index + thisJump;
    }
    sanity++;
    if(sanity > 90000000) {
        console.log('ABORT!!');
        inMaze = false;
    }
}