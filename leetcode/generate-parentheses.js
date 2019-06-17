/**
 * @param {number} n
 * @return {string[]}
 */
var generateParenthesis = function(n) {
    const result = [];
    makeBracket('', n * 2, result);
    
    return result.filter(check);
};

function makeBracket (current, n, result) {
    
    if(n === 0) {
        return result.push(current);
    }
    
    makeBracket(current + '(', n - 1, result);
    makeBracket(current + ')', n - 1, result);
}

function check(bracket) {
    const stack = [];
    
    for(let i=0; i<bracket.length; i++) {        
        if(bracket[i] === '(') stack.push(bracket[i]);
        else {
            if(stack.length === 0) return false;
            stack.pop();
        };
    }
    
    return stack.length === 0;
}
