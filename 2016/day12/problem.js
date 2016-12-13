let input = `cpy 1 a
cpy 1 b
cpy 26 d
jnz c 2
jnz 1 5
cpy 7 c
inc d
dec c
jnz c -2
cpy a c
inc a
dec b
jnz b -2
cpy c b
dec d
jnz d -6
cpy 17 c
cpy 18 d
inc a
dec d
jnz d -2
dec c
jnz c -5`;

let instructions = input.split('\n');
//problem 2 sets c to 1, problem 1 sets it to 0
let registers = {a:0, b:0, c:1, d:0 };

let sanity = 0;
for(var i=0;i<instructions.length;i++) {
    let instruction = instructions[i];
    //console.log(i+': '+instruction);
    
    if(instruction.indexOf('cpy') === 0) {
        let [,from,target] = instruction.split(' ');
    //    console.log('copy '+from+' to '+target);
        
        if(from === 'a') {
            registers[target] = registers["a"];
        } else if(from === 'b') {
            registers[target] = registers["b"];
        } else if(from === 'c') {
            registers[target] = registers["c"];
        } else if(from === 'd') {
            registers[target] = registers["d"];
        } else {
            registers[target] = Number(from);
        }
        
    }

    if(instruction.indexOf('inc') === 0) {
        let [,target] = instruction.split(' ');
  //      console.log('inc '+target);
        registers[target]++;
    }

    if(instruction.indexOf('dec') === 0) {
        let [,target] = instruction.split(' ');
//        console.log('dec '+target);
        registers[target]--;
    }

    if(instruction.indexOf('jnz') === 0) {
        /*
        jnz x y jumps to an instruction y away (positive means forward; negative means backward), but only if x is not zero
        */
        let [,x,y] = instruction.split(' ');
        if(registers[x]!=0) {
//            console.log('jump '+x+' '+y+' away');
            y--;
            i+=Number(y);
        }
    }

//    sanity++;
//    console.log(registers);
//    if(sanity > 300000) { console.log('EXIT'); process.exit(); }
}

console.log(registers);