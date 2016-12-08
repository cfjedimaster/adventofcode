
//screen size
let width = 7;
let height = 3;
let screen = seedScreen(width,height);

renderScreen(screen, width, height);

let input = 'rect 3x2';

screen = parseInput(input);

function parseInput(i) {
}

function seedScreen(w,h) {
    let screen = [];
    for(let i=0;i<w;i++) {
        for(let x=0;x<h;x++) {
            //console.log('setting s['+i+']['+x+']');
            if(!screen[i]) screen[i] = [];
            screen[i][x] = ".";
        }
    }
    return screen;
}

function renderScreen(s,width,height) {
    var result = '';
    for(let x=0;x<height;x++) {
        for(let i=0;i<width;i++) {
            result += s[i][x];
        }
        result += '\n';
    }
    console.log(result);
}