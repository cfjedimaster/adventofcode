const fs = require('fs');
const input = fs.readFileSync('./input.txt','utf8');
const shapes = input.split('\n');

var triangles = 0;

shapes.forEach(function(shape) {
    shape = shape.trim();
    shape = shape.replace(/ {2,}/g, " ");
    let sizes = shape.split(' ');
    let sidea = Number(sizes[0]);
    let sideb = Number(sizes[1]);
    let sidec = Number(sizes[2]);
    if(validTriangle(sidea,sideb,sidec)) triangles++;
//    console.log(sidea+' '+sideb+' '+sidec+' : '+validTriangle(sidea,sideb,sidec));
});

function validTriangle(a,b,c) {
    if((a+b) <= c) return false;
    if((a+c) <= b) return false;
    if((b+c) <= a) return false;
    return true;
}

//986 is too high
console.log(triangles);