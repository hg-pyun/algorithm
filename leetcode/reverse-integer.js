/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {  
    
    if(x === 0) return x;
    
    const sNumber = String(x);
    let result = [];
    
    let isNegative = false;
    for(let i = sNumber.length - 1; i >= 0; i--) {
        const c = sNumber[i];
        if(c === '-') {
            isNegative = true;
            continue;
        }
            
        result.push(c);
    }

    for(let i = 0; i<sNumber.length; i++) {
        const c = sNumber[i];
        if(c === '0')
            result.shift(c);
        else
            break;
    }
    
    if(isNegative)  result.unshift('-');
    
    const resultNum =  parseInt(result.join(''));
    if(resultNum > Math.pow(2,31) -1 || resultNum < -Math.pow(2,31)) return 0;
    
    return resultNum;
};
