

//console.log('  true is '+supportsSSL('aba[bab]xyz'));
//console.log('  false is '+supportsSSL('xyx[xyx]xyx'));
//console.log('  true is '+supportsSSL('zazbz[bzb]cdb'));
//console.log('  true is '+supportsSSL('aaa[kek]eke'));
//console.log(supportsSSL('bevtohpxkrlrjjen[jxnohlogvkugugmk]nrxomawkgbwlnqwb[rtjoeivssknwelkhv]dihcnpigtbnwfdlxhm'));

const fs = require('fs');
const input = fs.readFileSync('./input.txt','utf8');

let good = 0;
let lines = input.split('\n');
lines.forEach(function(line) {
    if(supportsSSL(line)) good++;
});
//259 is too high
console.log('Answer: '+good);


function findABA(s) {
    let results = [];
    //prev1 is 2 behind
    let prev1 = '';
    //prev2 is 1 behind
    let prev2 = '';
    let curr = '';

    for(let i=0;i<s.length;i++) {
        curr = s.substr(i,1);
        if(i > 0) prev2 = s.substr(i-1,1);
        if(i > 1) prev1 = s.substr(i-2,1);

        //check for aba if we have gone far enough
        if(i >= 2) {
            //console.log('does prev3 === prev2 '+(prev3===prev2));
            //if(prev3 === prev2) return false;
            //console.log('does prev1 eq curr? '+(prev1===curr));
            //console.log('does prev3 eq prev2? '+(prev2===prev3));
            if(curr !== ' ' && prev1 !== ' ' && prev2 != ' ' && curr !== prev2 && curr === prev1) results.push(prev1+prev2+curr);
        }
    }
    return results;
}

function supportsSSL(s) {

    /*
    first, get all the ABAs from s minus brackets
    */
    let matches = s.match(/\[.*?\]/g);
    for(let i=0;i<matches.length;i++) {
        s = s.replace(matches[i], ' ');
    }
    //now we have a clean string and bracket crap to check later
    let abas = findABA(s);

    //leave early
    if(abas.length === 0) return false;
    //now we are true if we can match the opposite of aba in brackets
    let bracketText = matches.join(' ').replace(/[\[\]]/g,'');
    for(let i=0;i<abas.length;i++) {
        let aba = abas[i];
        let bab = aba.substr(1,1) + aba.substr(0,1) + aba.substr(1,1);
//        console.log('bab is '+bab);
//        console.log('bracketText is '+bracketText+ ' idx of '+bracketText.indexOf(bab));
        if(bracketText.indexOf(bab) >= 0) return true;
    };
    return false;
}
