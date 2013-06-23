// :~$nodejs prime_numbers.js

var fs = require('fs');
outfile = 'prime_numbers.txt';
var isPrime = function( n ) {
if (n == 1 || n == 2) {
return true;
}
for (var i=2;i<n;i++) {
if (n % i == 0) {
return false;
}
}
return true;
}
var i =2;
n = 100;
var a = [];
while(true){
    var is_prime = isPrime(i)
    if(is_prime){
	//console.log('It is a prime number' + i);
	a.push(i);
	//console.log('Total prime is ' + a.length);
	if(a.length>=n)
	    break;
    }
    i = i + 1;
}
console.log(a.join());
fs.writeFileSync(outfile, a.join());
