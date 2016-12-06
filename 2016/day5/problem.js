var crypto = require('crypto');


var input = 'ojvtpuvg';
generatePassword(input);

function generatePassword(s) {
    console.log('input = '+s);
    let password = '';

    let i = -1;
    while(password.length < 8) {
        i++;
        var hash = crypto.createHash('md5').update(s + i).digest('hex');
        if(hash.indexOf('00000') === 0) {
            let pchar = hash.substr(5,1);
            password += pchar;
            console.log('Generating password: '+password);
        }
    }

    console.log('Final password: '+password);
}