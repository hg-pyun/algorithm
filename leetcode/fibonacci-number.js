/**
 * @param {number} N
 * @return {number}
 */
var fib = function(N) {
    const cache = new Map();
    return f(N, cache);
};

function f(n, cache) {
    if(n === 0) return 0;
    if(n === 1 || n === 2) return 1;
    if(cache.has(n)) return cache.get(n);
    
    const v = f(n - 1, cache) + f (n - 2, cache);
    cache.set(n, v);
    
    return v;
}
