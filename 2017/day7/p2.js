let testinput = `
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


const fs = require('fs');
let input = fs.readFileSync('./input.txt', 'UTF8');

// parse input
let lines = input.trim().split('\n');

let towers = {};

lines.forEach(line => {
    let parts = line.split(' ');
    let towerName = parts[0];
    let weight = Number(parts[1].replace(/[\(\)]/g,''));
    towers[towerName] = {};
    towers[towerName].weight = weight;
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

let towerNames = Object.keys(towers);

// ok, so the bottom one is one not held by another, how do we figure that out?
for(let i=0;i<towerNames.length;i++) {
    let weight = towerWeight(towers, towerNames[i]);
//    console.log('Weight of '+towerNames[i]+ ' is '+weight);
    towers[towerNames[i]].totalWeight = weight;
}

function towerWeight(towers, name) {
    let thisTower = towers[name];
    let weight = thisTower.weight;

    if(thisTower.holding) {
        let kidWeights = [];
        thisTower.holding.forEach(tower => {
            let kidWeight = towerWeight(towers, tower);
            weight += kidWeight;
            kidWeights.push(kidWeight);
        });
        let balanced=true;
    }
    return weight;
}

let root = '';

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
    if(!isHeld) {
        root = towerNames[i];
    }
};

console.log('Root is '+root);
findImbalance(towers,root);

function findImbalance(towers, name) {
    console.log('findImbalance('+name+')');
    let kids = towers[name].holding;
    if(isImbalanced(towers, kids)) {
        console.log('yes, imbalanced');
        let badKid = getImbalanced(towers, kids);
        console.log('badKid='+badKid);
        // ok, are my kids balanced?
        let kidsImbalanced = isImbalanced(towers, towers[badKid].holding);
        console.log('are my kids imb? '+kidsImbalanced);
        if(kidsImbalanced) {
            findImbalance(towers, badKid);
        } else {
            console.log('WINNER? ' + badKid);
            console.log(towers[badKid]);
            console.log('----');
            let badTower = towers[badKid];
            badTower.holding.forEach(t=>{
                console.log('t='+t);
                console.log(towers[t]);
            });
            console.log('----');
            console.log(towers['hnovowe']);
            console.log(towers['qsidq']);            
        }
    }
}

/*
Note ot myself in case I ever want to solve this again - solution is printed in the consoles above. You look at the weight
of the bad kid and it is 5 pounds too heavy, but enter into AoC the weight after removing 5
*/

function isImbalanced(towers, kids) {
    for(var i=1;i<kids.length;i++) {
        if(towers[kids[i]].totalWeight != towers[kids[i-1]].totalWeight) {
            return true;
        }
    }
    return false;
}

function getImbalanced(towers, kids) {
//    console.log('entering getImbalanxed with '+kids);
    /*
    ok, so given: [1,1,3,1,1] how do i know 3 is the bad guy?
    what if we loop over each:
        make a new array of everything else but current
        if avg is a whole number, im a bad guy?
    */
    for(var i=0;i<kids.length;i++) {
  //      console.log('checking '+kids[i]);
        let woMe = kids.slice();
        woMe.splice(i,1);
 //       console.log('woMe is now '+woMe);
        let sum = woMe.reduce(function(total,i) { 
//            console.log('i = '+towers[i].totalWeight);
            return total+towers[i].totalWeight; 
        } , 0);
        let avg = sum/woMe.length;
        if(avg === Math.round(avg)) {
            return kids[i];
        }
    }
}

process.exit(1);
/*
i dont know - it seems like if we look at a node and the kids weight dont match, that's it?
but - it has to have balanced kids
*/
for(let i=0;i<towerNames.length;i++) {
    let tower = towers[towerNames[i]];
//    console.log('check '+towerNames[i]);
    if(tower.holding) {
        for(var x=1; x< tower.holding.length;x++) {
            let thisTower = tower.holding[x];
            if(towers[thisTower].totalWeight !== towers[tower.holding[x-1]].totalWeight) {
                console.log('inbalence in '+towerNames[i]);
                console.log('i hold '+towers[towerNames[i]].holding);
                towers[towerNames[i]].holding.forEach(held => {
                    console.log('held='+held+' weight='+towers[held].totalWeight);
                    console.log(towers[held]);
                });
                //console.log(towers[towerNames[i]]);
            }
        }

    }
};

