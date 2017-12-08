
let cycle = 0;
//let banks = [0, 2, 7, 0];
let banks = [5,1,10,0,1,7,13,14,3,12,8,10,7,12,0,6];
let sanity = 0;
let done = false;

let seen = {};

while(!done) {
    //console.log('Banks: '+banks);

    cycle++;
    //first, find the biggest bank
    let biggestIdx = -1;
    let biggestValue = Number.MIN_VALUE;
    for(let i=0;i<banks.length;i++) {
        if(banks[i] > biggestValue) {
            biggestIdx = i;
            biggestValue = banks[i];
        }
    }

    //now redistribute
    //how much?
    let toShare = banks[biggestIdx];
    //clear it out
    banks[biggestIdx] = 0;
    let current = biggestIdx+1;
    if(current === banks.length) current = 0;
    while(toShare > 0) {
        banks[current]++;
        toShare--;
        current++;
        if(current === banks.length) current = 0;
    }

    // did we see this before?
    if(seen[banks.toString()]) {
        console.log('MATCH!');
        done = true;
    } else {
        seen[banks.toString()] = 1;
    }

    sanity++; if(sanity > 6666) { console.log('Abort'); process.exit(1); }
}

console.log('Done at cycle '+cycle);