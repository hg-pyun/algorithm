/**
 * @param {number} n
 * @return {number[]}
 */
var lexicalOrder = function(n) {
    
    const result = [];
    for(let i=1; i<10; i++) {
        dfs(i, n, result);
    }
    
    return result;
};

function dfs(cur, n, result) {
    if(cur > n) return;
    result.push(cur);
    
    for(let i=0; i<10; i++) {
        dfs(cur * 10 + i, n, result);
    }
}
