/*
let input = `value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2`;
*/
const fs = require('fs');
let input = fs.readFileSync('./input.txt','utf8');

let inputs = input.split('\n');

let bots = [];
let output = [];

function defineBot() {
    return {
        chips:[],
        logic:{'low':-1, 'high':-1}
    }
}

inputs.forEach(function(cmd) {
//    console.log('CMD: '+cmd);

    // value X goes to bot Y
    if(cmd.indexOf('value ') == 0) {
        let parts = cmd.split(' ');
        let value = parts[1];
        let bot = parts[5];
        if(!bots[bot]) bots[bot] = defineBot();

        bots[bot].chips.push(Number(value));
//        console.log('The bot is now: '+JSON.stringify(bots[bot]));
    }

    //bot X gives low to bot Y and high to bot Z
    //bot x gives low to OUTPUT Y
    if(cmd.indexOf('bot ') == 0) {
        let parts = cmd.split(' ');
        let owner = parts[1];

        if(!bots[owner]) bots[owner] = defineBot();

        bots[owner].logic.low = {target:parts[6], type:parts[5]};
        bots[owner].logic.high = {target:parts[11], type:parts[10]};
    }

});

//console.log(JSON.stringify(bots));
//process.exit(1);

//ok so in theory, we can process until we can't
var zz = 0;
while(hasStuffToDo(bots)) {
    for(let x=0;x<bots.length;x++) {
        let thisBot = bots[x];
        if(thisBot.chips.length == 2) {
//            console.log('processing bot '+JSON.stringify(thisBot));
            let sorted = thisBot.chips.sort((function(x,y) {
                if(x < y) return -1;
                if(x > y) return 1;
                return 0;
            }));
            let myLow = sorted[0];
            let myHigh = sorted[1];

            if(sorted[0] == 17 && sorted[1] == 61) {
                //13 is too low
                console.log('WINNER? '+x);
            }
//            console.log('my low is '+myLow+ ' and my high is '+myHigh);
            //hand stuf fout
            let lowTarget = thisBot.logic.low.target;
            let lowType = thisBot.logic.low.type;
            let highTarget = thisBot.logic.high.target;
            let highType = thisBot.logic.high.type;
            
            if(lowType === 'bot') {
//                console.log('hand my low chip to '+lowTarget);
                bots[lowTarget].chips.push(myLow);
            } else {
//                console.log('hand my low chip to output '+lowTarget);
                output[lowTarget] = myLow;
            }

            if(highType === 'bot') {
//                console.log('hand my high chip to '+highTarget);
                bots[highTarget].chips.push(myHigh);
            } else {
//                console.log('hand my high chip to output '+highTarget);
                output[highTarget] = myHigh;
            }

            bots[x].chips = [];
        }

    }
    zz++; if(zz > 100) { console.log('ABORT'); process.exit(); }
}

console.log('OUTPUT',output);

//I return true as long as one bot has 2 chips
function hasStuffToDo(bots) {
    for(var x=0;x<bots.length;x++) {
        if(bots[x].chips.length === 2) return true;
    }
    return false;
}

//Debug
/*
for(var x=0;x<bots.length;x++) {
    console.log('BOT '+x+' has chips '+bots[x].chips);
}
*/