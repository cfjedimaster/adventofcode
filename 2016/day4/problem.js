/*
var input = 'aaaaa-bbb-z-y-x-123[abxyz]';
console.log(validRoom(input));
console.log(validRoom('a-b-c-d-e-f-g-h-987[abcde]'));
console.log(validRoom('not-a-real-room-404[oarel]'));
console.log(validRoom('totally-real-room-200[decoy]'));
*/

const fs = require('fs');
const input = fs.readFileSync('./input.txt','utf8');
const rooms = input.split('\n');

let answer = 0;
rooms.forEach(function(room) {
    answer += validRoom(room);
});

console.log('answer = ' + answer);
/*
if true, returns sector, otherwise returns 0
*/
function validRoom(str) {
//    console.log('input = '+str);
    var parts = str.split('-');
    //first, get the room, which is all but the last
    var room = parts.slice(0, parts.length - 1).join('-');
    var endPart = parts[parts.length-1];
    var sector = Number(endPart.replace(/\[.+\]/g,''));
    var checksumInitial = endPart.replace(/.+\[(.*?)\].*/,'$1');
    //remove trailing newline, this could be done above I think
    checksumInitial = checksumInitial.replace(/\s/,'');
//    console.log('room='+room);
//    console.log('sector='+sector);
//    console.log(checksumInitial.length);
    /*
    now generate data on length of chars
    */
    var chars = [];

    for(var i=0;i<room.length;i++) {
        var char = room.substr(i,1);
        if(char === '-') continue;
        var curr = chars.findIndex(function(x) { return x.letter === char; });
        if(curr != -1) {
            chars[curr].size++;
        } else {
            chars.push({letter:char, size:1});
        }
    }

    //now generate checksum based on # of letters and alpha sort
    var sorted = chars.sort(function(a,b) {
        if(a.size > b.size) return -1;
        if(a.size < b.size) return 1;
        if(a.size === b.size) {
            if(a.letter > b.letter) return 1;
            if(a.letter < b.letter) return -1;
            return 0;
        }
        return 1;
    });
//    console.log(sorted);
    //checksum is just top 5
    var checksum = '';
//    console.log(sorted);
    for(var i=0;i<Math.min(5, sorted.length);i++) {
        checksum += sorted[i].letter;
    }
//    console.log('checksum='+checksum);
    if(checksum === checksumInitial) return sector;
    return 0;
}