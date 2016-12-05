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

rooms.forEach(function(room) {
    var isValid = validRoom(room);
    if(isValid.status) {
        //console.log('decrypt '+isValid.room);
        console.log(isValid.sector + ': '+caesarShift(isValid.room, isValid.sector).replace(/-/g,' '));
    }
});

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
    if(checksum === checksumInitial) {
        return {room:room, status:true, sector:sector};
    } else {
        return {status:false};
    }
}

//Credit: https://gist.github.com/EvanHahn/2587465
function caesarShift(str, amount) {

	// Wrap the amount
	if (amount < 0)
		return caesarShift(str, amount + 26);

	// Make an output variable
	var output = '';

	// Go through each character
	for (var i = 0; i < str.length; i ++) {

		// Get the character we'll be appending
		var c = str[i];

		// If it's a letter...
		if (c.match(/[a-z]/i)) {

			// Get its code
			var code = str.charCodeAt(i);

			// Uppercase letters
			if ((code >= 65) && (code <= 90))
				c = String.fromCharCode(((code - 65 + amount) % 26) + 65);

			// Lowercase letters
			else if ((code >= 97) && (code <= 122))
				c = String.fromCharCode(((code - 97 + amount) % 26) + 97);

		}

		// Append
		output += c;

	}

	// All done!
	return output;

};