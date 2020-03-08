/**
 * @param {number} rowIndex
 * @return {number[]}
 */

//    0,0
//  1,0, 1,1
//2,0, 2,1 ,2,2
var getRow = function(rowIndex) {
    const result = [];
    const memo = new Map();
    for(let col = 0; col <= rowIndex; col++) {
        result.push(pascal(rowIndex, col, memo));
    }
    
    return result;
};

function pascal(r, c, memo) {
    if(memo.has(`${r}.${c}`)) return memo.get(`${r}.${c}`);
    if(c === 0 || r === c) return 1;
    
    const v = pascal(r - 1, c - 1, memo) + pascal(r - 1, c, memo);
    memo.set(`${r}.${c}`, v);
    memo.set(`${r}.${r-c}`, v);
    return v;
}
