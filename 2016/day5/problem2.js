var crypto = require('crypto');


let input = 'ojvtpuvg';
generatePassword(input);

function generatePassword(s) {
    console.log('input = '+s);
    let password = ['','','','','','','',''];

    let i = -1;
    while(!passwordDone(password)) {
        i++;
        var hash = crypto.createHash('md5').update(s + i).digest('hex');
        if(hash.indexOf('00000') === 0) {
            let pchar = hash.substr(6,1);
            let pos = hash.substr(5,1);
            if(pos >= 0 && pos <= 7 && password[pos] === '') {
                console.log(hash, pchar, pos);
                password[pos] = pchar;
                console.log('Generating password: '+password);
            }
        }
    }

    console.log('Final password: '+password.join(''));
}

function passwordDone(inp) {
    for(i=0;i<inp.length;i++) {
        if(inp[i] === '') return false;
    }
    return true;
}