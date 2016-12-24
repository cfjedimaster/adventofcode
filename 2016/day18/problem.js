//let totalRows = 40;
//part 2
let totalRows = 400000;

let input = '.^.^..^......^^^^^...^^^...^...^....^^.^...^.^^^^....^...^^.^^^...^^^^.^^.^.^^..^.^^^..^^^^^^.^^^..^';

let room = [];

//let input = '.^^.^.^^^^';

room.push(input);

for(var i=0;i<totalRows-1;i++) {

    let newRow = getRow(room[room.length-1]);
    room.push(newRow);
}

//console.log(room);
let safeTiles = 0;
for(var i=0;i<room.length;i++) {
    let row = room[i];
    for(var x=0;x<row.length;x++) {
        let char = row.substr(x,1);
        if(char === '.') safeTiles++;
    }
}
//2047 is too high
console.log(safeTiles);

function getRow(input) {
    let newRow = '';
    for(var i=0;i<input.length;i++) {
        let left, center, right;
        if(i === 0) {
            left = '.';
        } else {
            left = input.substr(i-1,1);
        }
        center = input.substr(i,1);
        if(i < input.length -1) {
            right = input.substr(i+1,1);
        } else {
            right = '.';
        }
//        console.log('for '+i+ ' l='+left+' c='+center+' r='+right);

        if(
            (left === '^' && center === '^' && right === '.')
            ||
            (center === '^' && right === '^' && left === '.')
            ||
            (left === '^' && center === '.' && right === '.')
            ||
            (right === '^' && left === '.' && center === '.')
        ) {
            newRow += '^';
        } else {
            newRow += '.';
        }

    }
    return newRow;
}