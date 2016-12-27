/*
https://www.reddit.com/r/adventofcode/comments/5ifn4v/2016_day_15_solutions/db7ttta/
*/

function d1(t) { return ((t+2) % 5 == 0); };
function d2(t) { return ((t+7) % 13 == 0); };
function d3(t) { return ((t+10) % 17 == 0); };
function d4(t) { return ((t+2) % 3 == 0); };
function d5(t) { return ((t+9) % 19 == 0); };
function d6(t) { return ((t+0) % 7 == 0); };
function d7(t) { return ((t+0) % 11 == 0); };

let t = 0;
while(true) {
	if(
		d1(t+1) &&
		d2(t+2) &&
		d3(t+3) &&
		d4(t+4) &&
		d5(t+5) &&
		d6(t+6) &&
		d7(t+7)
	) {
		console.log(t);
		process.exit();
	}
	t++;
}