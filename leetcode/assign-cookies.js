/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function(g, s) {
    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);
    
    let cursor = 0;
    let r = 0;
    for(let i = 0; i< s.length; i++) {
        if(g[cursor] <= s[i]){
            r++;
            cursor++;
        }
    }
    
    return r;
};
