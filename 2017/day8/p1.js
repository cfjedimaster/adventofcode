let input_test = `
b inc 5 if a > 1
a inc 1 if b < 5
c dec -10 if a >= 1
c inc -20 if c == 10
`

const fs = require('fs');
let input = fs.readFileSync('./input.txt', 'UTF8');


let registers = {};

let instructions = input.trim().split('\n');
console.log('Processing '+instructions.length+ ' instructions.');
instructions.forEach(ins => {
    let parts = ins.split(' ');
    let register = parts[0];
    let action = parts[1];
    let amount = Number(parts[2]);
    let condRegister = parts[4];
    let op = parts[5];
    let condCheck = parts[6];

    //if no register, set to 0
    if(!registers[register]) registers[register] = 0;
    if(!registers[condRegister]) registers[condRegister] = 0;

    //console.log(`${registers[condRegister]} ${op} ${condCheck}`);

    if(eval(`${registers[condRegister]} ${op} ${condCheck}`)) {
        if(action === 'inc') {
            registers[register] += amount;
        } else if(action === 'dec') {
            registers[register] -= amount;
        }
    } else {
        //console.log('false');
    }
});

console.log(registers);
let keys = Object.keys(registers);
let largest = Number.MIN_VALUE;
keys.forEach(key => {
    if(registers[key] > largest) largest = registers[key];
});

console.log('Largest='+largest);