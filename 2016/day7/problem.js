

//console.log('  true is '+supportsTSL('abba[mnop]qrst'));
//console.log('  false is '+supportsTSL('abcd[bddb]xyyx'));
//console.log('  false is '+supportsTSL('aaaa[qwer]tyui'));
//console.log('  true is '+supportsTSL('ioxxoj[asdfgh]zxcvbn'));

const fs = require('fs');
const input = fs.readFileSync('./input.txt','utf8');

let good = 0;
let lines = input.split('\n');
lines.forEach(function(line) {
    if(supportsTSL(line)) good++;
});
console.log('Answer: '+good);

function hasABBA(s) {
    //prev1 is 3 behind
    let prev1 = '';
    //prev2 is 2 behind
    let prev2 = '';
    //prev3 is 1 behind
    let prev3 = '';
    let curr = '';
    for(let i=0;i<s.length;i++) {
        curr = s.substr(i,1);
        if(i > 0) prev3 = s.substr(i-1,1);
        if(i > 1) prev2 = s.substr(i-2,1);
        if(i > 2) prev1 = s.substr(i-3,1);
        //check for abba if we have gone far enough
        if(i >= 3) {
            //console.log('abba? '+prev1+prev2+prev3+curr);
            //console.log('does prev3 === prev2 '+(prev3===prev2));
            //if(prev3 === prev2) return false;
            //console.log('does prev1 eq curr? '+(prev1===curr));
            //console.log('does prev3 eq prev2? '+(prev2===prev3));
            if(prev1 === curr && prev2 === prev3 && prev1 !== prev2) return true;
        }
    }
    return false;
}

function supportsTSL(s) {

    //must have a string of the form xyyx (x cannot be y) (ABBA)
    //must NOT have such a thing inside sq brackets
    //so first, get all the blocks INSIDE [], and see if they have ABBA, if so, FALSE
    //then look at the rest  

    let matches = s.match(/\[.*?\]/g);
    for(let i=0;i<matches.length;i++) {
        let match = matches[i].replace(/[\[\]]/g, '');
//        console.log('check ABBA for '+match + '='+hasABBA(match));
        if(hasABBA(match)) return false;
        s = s.replace(matches[i], ' ');
    }
//    console.log('pass bracket, now we have '+s);
    return hasABBA(s);
}