const fs = require('fs');
const input = fs.readFileSync('./input.txt','utf8');
const input1 = `101 301 501
102 302 502
103 303 503
201 401 601
202 402 602
203 403 603`;

/*
now we need to make a new list of inputs based on columns
*/
let shapes = [];
//var colA = []; var colB = []; var colC = [];
const lines = input.split('\n');

let colA = [];
let colB = [];
let colC = [];

lines.forEach(function(line) {
    line = line.trim();
    line = line.replace(/ {2,}/g, " ");
    let inputs = line.split(' ');
    colA.push(inputs[0]); colB.push(inputs[1]); colC.push(inputs[2]);
});

// now we have 3 arrays of input we need to add to shapes
function makeShapes(inp) {
    let results = [];
    for(var i=0;i<inp.length;i+=3) {
        results.push({sidea:Number(inp[i]), sideb:Number(inp[i+1]), sidec:Number(inp[i+2])});
    }
    return results;
}

shapes = shapes.concat(makeShapes(colA));
shapes = shapes.concat(makeShapes(colB));
shapes = shapes.concat(makeShapes(colC));
console.log('shapes = '+shapes.length);

var triangles = 0;

shapes.forEach(function(shape) {
    if(validTriangle(shape.sidea,shape.sideb,shape.sidec)) triangles++;
//    console.log(shape.sidea+' '+shape.sideb+' '+shape.sidec+' : '+validTriangle(shape.sidea,shape.sideb,shape.sidec));
});

function validTriangle(a,b,c) {
    if((a+b) <= c) return false;
    if((a+c) <= b) return false;
    if((b+c) <= a) return false;
    return true;
}

console.log(triangles);

