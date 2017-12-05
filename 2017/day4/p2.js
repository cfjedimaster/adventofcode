
/*
let passphrases = [
    'aa bb cc dd ee',
    'aa bb cc dd aa',
    'aa bb cc dd aaa'
];
*/
const fs = require('fs');
let passphrases = fs.readFileSync('./passphrases.txt', 'UTF8').split('\n');

let totalGood = 0;

passphrases.forEach(p => {
    if(isGood(p)) {
        totalGood++;
        console.log(p+': GOOD!');
    } else console.log(p+': bad');
});
console.log('Total good is '+totalGood);

function isGood(p) {
    let words = p.split(/\s/);
    //convert all words to a new string sorted alpha
    words = words.map(word => {
        return word.toLowerCase().split('').sort().join('');
    });
    let used = [];
    for(var i=0;i<words.length;i++) {
        let word = words[i];
        if(used.indexOf(word) !== -1) return false;
        used.push(word);
    };
    return true;
}