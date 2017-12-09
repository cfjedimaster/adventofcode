/*
let input = `
pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
`;
*/

const fs = require('fs');
let input = fs.readFileSync('./input.txt', 'UTF8');

// parse input
let lines = input.trim().split('\n');

let towers = {};

lines.forEach(line => {
    let parts = line.split(' ');
    let towerName = parts[0];
//    console.log('towerName',towerName);
    towers[towerName] = {};
    if(parts.length >= 3) {
        parts.splice(0,3);
        //remove trailing commas
        parts = parts.map(p => {
            return p.replace(/,/g,'');
        });
        towers[towerName].holding = parts;
    }
});

//console.log(towers);

// ok, so the bottom one is one not held by another, how do we figure that out?
let towerNames = Object.keys(towers);
for(let i=0;i<towerNames.length;i++) {
    //console.log('is tower '+towerNames[i]+' held by someone?');
    let isHeld = false;
    for(let x=0;x<towerNames.length;x++) {
        if(x !== i) {
            if(towers[towerNames[x]].holding && towers[towerNames[x]].holding.includes(towerNames[i])) {
                isHeld = true;
                break;
            }
        }
    }
    //console.log('is Held? '+isHeld);
    if(!isHeld) console.log(towerNames[i]);
};