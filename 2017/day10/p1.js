
let skipSize = 0;
let input = '165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153';
//size of knot
let string = 256;
let currentPos = 0;

//turn input into array
input = input.split(',');
input = input.map(i=> {
    return Number(i);
});

//create initial list
let list = [];
for(var i=0;i<string;i++) {
    list[i] = i;
}
console.log('list is '+list+'\n');

// loop over input
for(var i=0; i<input.length; i++) {
    let toSel = input[i];
    console.log('toSel '+toSel);
    if(toSel !== 1) {
        //create an array of positions 
        let selectedValues = [];
        let marker = currentPos-1;
        for(var x=0;x<toSel;x++) {
            marker++;
            if(marker+1 > string) marker = 0;       
            //console.log('marker='+marker+' x is '+x);
            selectedValues.push(list[marker]);
        }
        //console.log('selectedValues '+selectedValues);
        selectedValues.reverse();
        //console.log('reversed selectedValues '+selectedValues);
        //update list
        marker = currentPos-1;
        for(var x=0;x<toSel;x++) {
            marker++;
            if(marker+1 > string) marker = 0;
            //console.log('updating list at pos '+marker+' to set value '+selectedValues[x]);
            list[marker] = selectedValues[x];
        }
    }
    //console.log('List is now: '+list);
    let toMove = toSel+skipSize;
    for(var x=0;x<toMove;x++) {
        currentPos++;
        if(currentPos === string) currentPos=0;
    }
    //console.log('currentPos='+currentPos);
    skipSize++;
    //console.log('\n');
}

let result = list[0]*list[1];
console.log('RESULT='+result);