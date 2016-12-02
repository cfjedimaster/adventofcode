const fs = require('fs');
const input = fs.readFileSync('./input.txt','utf8');
//const input = 'RRRRDDDDLLLLLL';
const instructions = input.split('\n');

let curPos = [1, 1];
var pressed = [];
instructions.forEach(function(instruction) {

    for(var i=0;i<instruction.length;i++) {
        let d = instruction.substring(i,i+1);
        curPos = move(curPos,d);
    }

    pressed.push(button(curPos));

});

console.log(pressed.join(''));

/*
basically just ensure we don't go too far off the edge
values are RLUD

    1
  2 3 4
5 6 7 8 9
  A B C
    D
*/
function move(pos, dir) {
    var orig = Array.from(pos);
    let grid = [
        "  D  ",
        " ABC ",
        "56789",
        " 234 ",
        "  1  "];

    if(dir === "R" && pos[0] < 4) {
        pos[0]++;
    }
    if(dir === "L" && pos[0] > 0) {
        pos[0]--;
    }
    if(dir === "U" && pos[1] < 4) {
        pos[1]++;
    }
    if(dir === "D" && pos[1] > 0) {
        pos[1]--;
    }

    //if value is blank, we don't move
    let row = grid[pos[0]];
    let picked = row.substring(pos[1], pos[1]+1);
    if(picked === " ") {
        return orig;
    } 
    return pos;
}

/*
translate position to button
    1
  2 3 4
5 6 7 8 9
  A B C
    D

*/
function button(p) {
    var l = p.toString();
    if(l === "2,4") return 1;
    if(l === "1,3") return 2;
    if(l === "2,3") return 3;
    if(l === "3,3") return 4;
    if(l === "0,2") return 5;
    if(l === "1,2") return 6;
    if(l === "2,2") return 7;
    if(l === "3,2") return 8;
    if(l === "4,2") return 9;
    if(l === "1,1") return "A";
    if(l === "2,1") return "B";
    if(l === "3,1") return "C";
    if(l === "2,0") return "D";
    console.log('BAD '+l); process.exit();
}