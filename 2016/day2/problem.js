const fs = require('fs');
const input = fs.readFileSync('./input.txt','utf8');
//const input = 'RRRRDDDDLLLLLL';
const instructions = input.split('\n');

/*
1 2 3
4 5 6
7 8 9
*/

let curPos = [1, 1];
var pressed = [];
instructions.forEach(function(instruction) {

    for(var i=0;i<instruction.length;i++) {
        let d = instruction.substring(i,i+1);
        curPos = move(curPos,d);
        //console.log(curPos);
    }
    
    pressed.push(button(curPos));

});

console.log(pressed.join(''));

/*
basically just ensure we don't go too far off the edge
values are RLUD
*/
function move(pos, dir) {

    if(dir === "R" && pos[0] < 2) {
        pos[0]++;
    }
    if(dir === "L" && pos[0] > 0) {
        pos[0]--;
    }
    if(dir === "U" && pos[1] < 2) {
        pos[1]++;
    }
    if(dir === "D" && pos[1] > 0) {
        pos[1]--;
    }
    return pos;
}

/*
translate position to button
1 2 3
4 5 6
7 8 9
*/
function button(p) {
    var l = p.toString();
    if(l === "0,2") return 1;
    if(l === "1,2") return 2;
    if(l === "2,2") return 3;
    if(l === "0,1") return 4;
    if(l === "1,1") return 5;
    if(l === "2,1") return 6;
    if(l === "0,0") return 7;
    if(l === "1,0") return 8;
    if(l === "2,0") return 9;

}