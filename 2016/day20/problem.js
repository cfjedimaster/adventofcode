const fs = require('fs');
const input = fs.readFileSync('./input.txt','utf8');

let gates = [];
let lines = input.split('\n');

const MAX = 4294967295;

lines.forEach((l)=>{
    let [min,max] = l.split('-');
    gates.push({min:Number(min), max:Number(max)});
});

gates.sort(function(a, b) {
    if(a.min < b.min) return -1;
    if(a.min > b.min) return 1;
    return 0;
});

console.log('len is '+gates.length);


//simplify gates
for(var i=1;i<gates.length;i++) {

    let thisGate = gates[i];
    let lastGate = gates[i-1];

    /*
    imagine: 
    last 0-100
    this: 49-150

    we can say that's the same as 0-150

    imagine:
    last 0-100
    this: 101-150 
    */
    if(
        (thisGate.min > lastGate.min && thisGate.min < lastGate.max && thisGate.max > lastGate.max && thisGate.max <= MAX) 
        ||
        (thisGate.min-1 == lastGate.max && thisGate.max <= MAX)) {
        let newGate = { min:lastGate.min, max:thisGate.max};
        // remove i
        gates[i-1] = newGate;
        gates.splice(i, 1);
        //reset i
        i=0;
    }
}

console.log('new len is '+gates.length);
/*
if(gates.length < 10) {
    gates.forEach(function(g) {
        console.log('Min='+format(g.min) + ' Max='+format(g.max));
    });
} else {
    console.log(gates[0]);
    console.log(gates[1]);
}
*/

//console.log('Winner='+format(gates[0].max+1));
console.log('Winner='+(gates[0].max+1));

function format(r) {
    return new Intl.NumberFormat().format(r);
}
