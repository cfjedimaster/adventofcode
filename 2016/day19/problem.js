//let numElves = 5;
let numElves = 3005290;
let elves = [];

for(var i=0;i<numElves;i++) {
    elves[i] = 1;
}

let done = false;

let sanity = 0;
while(!done) {

    //go around
    for(var i=0;i<numElves;i++) {
        let nextElfPos;
//        console.log('Working with elf '+(i+1));
        if(elves[i] > 0) {
            /*
            if(i < numElves-1) {
                nextElfPos = i+1;
            } else {
                nextElfPos = 0;
            }
            */
            // nextElfPos is the next elf with presents

            if(i < numElves-1) {
                nextElfPos = i+1;
            } else {
                nextElfPos = 0;
            }
            while(elves[nextElfPos] === 0) {
                nextElfPos++;
                if(nextElfPos == numElves) nextElfPos = 0;
            }

            elves[i] += elves[nextElfPos];
            elves[nextElfPos] = 0;
//            console.log('Took from elf '+(nextElfPos+1));
            if(elves[i] === numElves) {
                console.log('Winner for '+(i+1));
                process.exit();
            }
        } else {
//            console.log('No presents, skipping.');
        }            
    }
    sanity++;
    if(sanity > 2000) { console.log('Abort'); process.exit(); }
}