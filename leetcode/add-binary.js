/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    
    if(a.length > b.length) {
        b = fillWithZero(b, a.length - b.length);
    }
    else {
        a = fillWithZero(a, b.length - a.length);
    }
    
    let r = [];
    let carry = 0;
    for(let i = a.length - 1; i >= 0; i--) {
        const numA = Number(a[i]);
        const numB = Number(b[i]);
        
        const sum = numA + numB + carry;

        switch (sum) {
            case 0: 
                r.push(0);
                carry = 0;
                break;
            case 1: 
                r.push(1);
                carry = 0;
                break;
            case 2:
                r.push(0);
                carry = 1;
                break;
            case 3:
                r.push(1);
                carry = 1;
                break;
                
        }
    }
    
    carry === 1 && r.push(carry);
    
    return r.reverse().join('');
};

function fillWithZero (n, length) {
    let zeroDigit = ""
    for(let i = 0; i < length; i++) {
        zeroDigit += "0";
    }
    return zeroDigit + n;
}
