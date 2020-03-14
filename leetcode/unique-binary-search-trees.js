/**
 * @param {number} n
 * @return {number}
 */
var numTrees = function(n) {
    const g = new Array(n+1).fill(0);
    g[0] = g[1] = 1;
    
    for(let i = 2; i <= n; i++ ) {
        for(let j = 1; j <= i; j++) {
            g[i] += g[j-1] * g[i-j];
        }
    }
    
    return g[n];
};
