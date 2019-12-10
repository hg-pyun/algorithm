/**
 * @param {number} n
 * @return {string[]}
 */
var fizzBuzz = function(n) {
    const r = [];
    for(let i = 1; i <= n; i++) {
        if(i % 3 == 0 && i % 5 === 0) {
            r.push("FizzBuzz");
        }
        else if(i % 3 === 0) {
            r.push("Fizz");
        }
        else if(i % 5 === 0) {
            r.push("Buzz");
        }
        else {
            r.push(i.toString());
        }
    }
    return r;
};
