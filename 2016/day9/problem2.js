

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
//console.log('XABCABCABCABCABCABCY'==decompress('X(8x2)(3x3)ABCY'));
//console.log(decompress('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN').length);

const fs = require('fs');
let input = fs.readFileSync('./input.txt','utf8');
//this should be one line
input = input.replace(/ /g, '');
input = input.replace(/\n/g, '');


let result = decompress(input);
console.log(result);
//final answer: 11,658,395,076

function decompress(s) {
    let matches = s.match(/\(\d+x\d+\)/);
    if(!matches) return s;
    let result = 0;

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
        */
        result += (s.substr(0, matches.index)).length;
//        console.log('result so far = '+result);
        if(result % 500000 === 0) console.log(result);
//        result += repeated;
//        console.log('result so far = '+result);
        //the last part is a bit more complex
        //we need to know the number here so we can search past it later
        minMatch = matches.index + matches[0].length + numChar;
//        console.log('lastPart num is ',minMatch);
        let lastPart = s.substr(minMatch);
//        console.log('lastPart',lastPart);
        s = repeated += lastPart;

        matches = s.match(/\(\d+x\d+\)/);
        //will we continue?
        if(!matches) result += s.length;
    }
    return result;
}
