/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    const memo = new Map();
    return f(n, memo);
};

function f(n, memo) {
    if(memo.has(n)) return memo.get(n);
    if(n === 1) return 1;
    if(n === 2) return 2;
    
    const v = f(n - 1, memo) + f(n - 2, memo);
    memo.set(n, v);
    
    return v;
}
