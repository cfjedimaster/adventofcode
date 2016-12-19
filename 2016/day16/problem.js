
let input = '10001110011110000';
//let neededSize = 272;
let neededSize = 35651584;

let result = input;
while(result.length <= neededSize) {
    result = doIt(result);
}

console.log('Done with initial...');
//we only want neededSize

result = result.substr(0, neededSize);

console.log('Checksum:');
console.log(checkSum(result));

//console.log(doIt('111100001010')=='1111000010100101011110000');


function doIt(a) {
    let b = reverse(a);
    //prob could be regex
    let newB = '';
    for(let i=0;i<b.length;i++) {
        let char = b.substr(i, 1);
        if(char === '1') {
            newB += '0';
        } else if(char === '0') {
            newB += '1';
        } else newB += char;
    }
    return a + '0' + newB;
}

function reverse(s) {
    let result = '';
    for(let i=0;i<s.length;i++) {
        result = s.substr(i,1) + result;
    }
    return result;
}

function checkSum(s) {
    let done = false;
    while(!done) { 
        let checksum = '';
        for(var i=0;i<s.length;i=i+2) {
            let set1 = s.substr(i,1);
            let set2 = s.substr(i+1,1);
            if(set1 === set2) checksum += '1';
            else checksum += '0'; 
        }
        if(checksum.length % 2 === 1) {
            return checksum;
        } else {
            s = checksum;
        }
    }
}