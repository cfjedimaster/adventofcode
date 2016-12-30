//let numElves = 5;
let numElves = 3005290;
let elves = [];

for(var i=0;i<numElves;i++) {
    elves[i] = {name:i+1,gifts:1};
}

let done = false;

let sanity = 0;
while(!done) {
    console.log('\nSize of elves is '+elves.length);
    //go around
    for(var i=0;i<elves.length;i++) {

        if(i % 10000 === 0) {
            process.stdout.write('#');
        }
//        console.log('\nWorking with elf '+(elves[i].name));
        /*
        the elf across from me is:
            floor(len/2)+1 offset
        */
        let pos = Math.floor(elves.length/2)+1;
//        console.log('pos is '+pos);
        //add my pos
        pos += i;


        //now fix for len
        if(pos > elves.length) pos = pos - elves.length;
//        console.log('adjusted pos is '+pos);
//        console.log('Taking from Elf '+elves[pos-1].name);
        elves[i].gifts += elves[pos-1].gifts;
//        console.log('Elf '+(elves[i].name) +' now has '+elves[i].gifts + ' gifts.');

//        console.log(elves); 
        if(elves[i].gifts === numElves) {
            console.log('Winner for '+(i+1));
            console.log(elves[i]);
            process.exit();
        }

        //now remove em
        elves.splice(pos-1, 1);   
        
    }

    sanity++;
    if(sanity > 400) { console.log('Abort'); process.exit(); }
}