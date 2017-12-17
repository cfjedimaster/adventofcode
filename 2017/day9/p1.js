/*
I failed and used this solution:
https://www.reddit.com/r/adventofcode/comments/7iksqc/2017_day_9_solutions/dqziw0i/
*/

/*
{}, score of 1.
{{{}}}, score of 1 + 2 + 3 = 6.
{{},{}}, score of 1 + 2 + 2 = 5.
{{{},{},{{}}}}, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
{<a>,<a>,<a>,<a>}, score of 1.
{{<ab>},{<ab>},{<ab>},{<ab>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<!!>},{<!!>},{<!!>},{<!!>}}, score of 1 + 2 + 2 + 2 + 2 = 9.
{{<a!>},{<a!>},{<a!>},{<ab>}}, score of 1 + 2 = 3.
*/
/*
let inputs = [
    '{}', 
    '{{{}}}', 
    '{{},{}}', 
    '{{{},{},{{}}}}',
    '{<a>,<a>,<a>,<a>}',
    '{{<ab>},{<ab>},{<ab>},{<ab>}}',
    '{{<!!>},{<!!>},{<!!>},{<!!>}}', 
    '{{<a!>},{<a!>},{<a!>},{<ab>}}'
];
*/
const fs = require('fs');
let inputs = [];

let inp = fs.readFileSync('./input.txt', 'UTF8');

inputs[0] = input;

// 446790 is too high
inputs.forEach(input => {

    //console.log(input);
    input = removeGarbage(input);
    console.log(input);
    score = getScore(input);
    console.log('score='+score);

});

function removeGarbage(s) {
    //first remove !X
    s = s.replace(/\!./g,'');
    //remove <...>
    s = s.replace(/<.*?>/g,'');
    return s;
}

function getScore(s) {
    let score = 0;
    let i = 1;
    let chars = s.split('');
    for(let x=0;x<chars.length;x++) {
        let thisChar = chars[x];
        if(thisChar === '{') {
            if(x >= 1) {
                if(chars[x-1] === '{') i++;
            }
            score += i;
        }
        if(thisChar === '}') {
            //i--;
        }
        //console.log(x,i);
    }
    return score;
}