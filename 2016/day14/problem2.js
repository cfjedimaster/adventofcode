
/*
https://www.reddit.com/r/adventofcode/comments/5ioh1b/2016_day_14_part_1_missing_something_stupid_im/
credit goes to 
    https://www.reddit.com/user/the4ner
and
https://www.reddit.com/user/AustinVelonaut
*/

var crypto = require('crypto');

let input = 'qzyelonm';
//let input = 'abc';

let threeKeys = {};
let keys = [];

function makeHash(s) {
	for(var x=0;x<2017;x++) {
		s = crypto.createHash('md5').update(s).digest('hex').toLowerCase();
	}
	return s;
}

for(var i=0;i<999999;i++) {
    let test = input + i;
//    let hash = crypto.createHash('md5').update(test).digest('hex').toLowerCase();
	let hash = makeHash(test);
	if(i % 2000 === 0) process.stdout.write('#');
    let matches5 = hash.match(/(\w)(\1{4})/);

    if(matches5) {
        let match = matches5[0];
        let smatch = match.substr(0,3);

        if(threeKeys[smatch]) {

            let threeKey = threeKeys[smatch];

            for(var x=0;x<threeKey.length;x++) {

                if(i - threeKey[x] <= 1000) {
                    keys.push(threeKey[x]);
                    if(keys.length === 900) {

                        keys = keys.sort(function(a,b) {
                            if(a > b) return 1;
                            if(a < b) return -1;
                            return 0;
                        });
						process.stdout.write('\n');
                        console.log(keys[63]);
                        process.exit();
                    }
                }
            }

            delete threeKeys[smatch];
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