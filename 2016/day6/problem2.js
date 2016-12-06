
const fs = require('fs');
const input = fs.readFileSync('./input.txt','utf8');


let cols = [];
let lines = input.split('\n');

lines.forEach(function(line) {
    for(let i=0;i<line.length;i++) {
        let char = line.substr(i,1);
        if(!cols[i]) cols[i] = [];
        cols[i].push(char);
    }
});

//console.log(cols);

let solution = '';

// Now go through each col and count
for(let i=0;i<cols.length;i++) {
    let count = {};
    for(let j=0;j<cols[i].length;j++) {
        let letter = cols[i][j];
        if(!count[letter]) count[letter] = 0;
        count[letter]++;
    }
    var lowest = 9999999;
    var selected = '';
    for(var key in count) {
        if(count[key] < lowest) {
            selected = key;
            lowest = count[key];
        }
    }
    solution += selected;
}

console.log(solution);