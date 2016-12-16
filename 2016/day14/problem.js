var crypto = require('crypto');


//let input = 'qzyelonm';
let input = 'abc';

let threeKeys = {};
let keys = [];

for(var i=0;i<(110+1001);i++) {
    let test = input + i.toString();
    let hash = crypto.createHash('md5').update(test).digest('hex').toLowerCase();
    let matches5 = hash.match(/(\w)(\1{4})/);
if(hash.indexOf('999') >= 0) console.log(i+':'+hash);
    if(matches5) {
        let match = matches5[0];
        let smatch = match.substr(0,3);
if(match === '99999') console.log(i);
        if(threeKeys[smatch]) {

            let threeKey = threeKeys[smatch];

            for(var x=0;x<threeKey.length;x++) {

                if(i - threeKey[x] <= 1000) {
                    keys.push(threeKey[x]);
                    threeKeys[smatch].shift();

                    if(keys.length === 64) {
                        console.log('i='+i+' idx = '+keys[63]);                

                        keys = keys.sort(function(a,b) {
                            if(a > b) return 1;
                            if(a < b) return -1;
                            return 0;
                        });
                        console.log(keys.slice(0,10)); 

                        process.exit();
                    }
                    break;
                }
            }

        }
    }


    let matches = hash.match(/(\w)(\1{2})/);
    if(matches) {
        let match = matches[0];
        if(!threeKeys[match]) {
            threeKeys[match] = [i];
        } else {
            threeKeys[match].push(i);
        }
    }

}