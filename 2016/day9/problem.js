

//console.log(decompress('ADVENT'));
//console.log('-------------------------');
//console.log(decompress('A(1x5)BC'));
//console.log('-------------------------');
//console.log(decompress('(3x3)XYZ'));
//console.log('-------------------------');
/*
console.log('ABCBCDEFEFG' == decompress('A(2x2)BCD(2x2)EFG'));
console.log('-------------------------');

console.log('(1x3)A' == decompress('(6x1)(1x3)A'));
console.log('-------------------------');

console.log('X(3x3)ABC(3x3)ABCY' == decompress('X(8x2)(3x3)ABCY'));
console.log('-------------------------');
*/
const fs = require('fs');
let input = fs.readFileSync('./input.txt','utf8');
//this should be one line
input = input.replace(/ /g, '');
input = input.replace(/\n/g, '');


// 120767 is too high
let result = decompress(input);
console.log(result.length);

function decompress(s) {
    let matches = s.match(/\(\d+x\d+\)/);
    if(!matches) return s;
    let result = '';

    while(matches) {
//        console.log(matches);
        let marker = matches[0].replace(/[\(\)]/g,'');
        let [numChar, numRep] = marker.split('x');
//        console.log('marker='+marker, numChar, numRep);
        numChar = Number(numChar); numRep = Number(numRep);

        let stringToRepeat = s.substr(matches.index+matches[0].length, numChar);
        let repeated = stringToRepeat.repeat(numRep);
//        console.log('stringToRepeat='+stringToRepeat, repeated);
        /*
        new string is:
        0-Where I found match
        Repeated String
        0 + Where I found match + length of match + length of string to repeat

        TO the end
        */
        result += s.substr(0, matches.index);
//        console.log('result so far = '+result);
        result += repeated;
//        console.log('result so far = '+result);
        //the last part is a bit more complex
        //we need to know the number here so we can search past it later
        minMatch = matches.index + matches[0].length + numChar;
//        console.log('lastPart num is ',minMatch);
        let lastPart = s.substr(minMatch);
//        console.log('lastPart',lastPart);
        s = lastPart;

        matches = s.match(/\(\d+x\d+\)/);
        //will we continue?
//        console.log(matches);
//        console.log('\n\n');
        if(!matches) result += s;
    }
    return result;
}

