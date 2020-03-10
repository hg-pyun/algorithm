/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    if(n === 0) return 1;
    
    const c = pow(x, Math.abs(n));
    return n > 0 ? c : 1/c
};

function pow(x, n) {
    console.log(x, n)
    if(n === 1) return x;
    return n % 2 === 0 ? pow(x*x, n/2) : x * pow(x*x, Math.floor(n/2))
}
