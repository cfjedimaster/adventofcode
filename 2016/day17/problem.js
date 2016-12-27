var crypto = require('crypto');

function hash(s) {
    return crypto.createHash('md5').update(s).digest('hex');
}

let pos = {x:1, y:1};

var input = 'njfxhljp';
let path = '';

let sanity = 0;
let doIt = true;
while(doIt) {

    var h = hash(input);
    var dir = h.substr(0,4);
    console.log(dir);

    let doors = checkDoors(dir);
    console.log(doors);
    // prefer R or D if we can
    if(doors.d && pos.y <=3) {
        console.log('move down');
        pos.y++;
        input += 'D';
        path += 'D';
    } else if(doors.r && pos.x <= 3) {
        console.log('move right');
        pos.x++;
        input += 'R';
        path += 'R';
    } else if(doors.u && pos.y > 1) {
        console.log('move up');
        pos.y--;
        input += 'U';
        path += 'U';
    } else if(doors.l && pos.x > 1) {
        console.log('move left');
        pos.x--;
        input += 'L';
        path += 'L';
    }

    //are we at 4 4?
    if(pos.x === 4 && pos.y === 4) {
        console.log('WIN');
        console.log(path);
        doIt = false;
    }

    sanity++; if(sanity > 10) process.exit();
}

function checkDoors(s) {
    let u = s.substr(0,1);
    let d = s.substr(1,1);
    let l = s.substr(2,1);
    let r = s.substr(3,1);

    let result = {};
    result.u = isOpen(u);
    result.d = isOpen(d);
    result.l = isOpen(l);
    result.r = isOpen(r);
    return result;
}

function isOpen(x) {
    if(x === 'b' || x === 'c' || x === 'd' || x === 'e' || x === 'f') return true;
    return false;
}