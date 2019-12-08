/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    
    if(x < 0)
        return false;
    
    const s = x.toString();
    
    let f = 0;
    let l = s.length - 1;
    let r = true;

    while(f < l) {
        if(s[f] !== s[l]) {
            r = false;
            break;
        }
        f++;
        l--;
    }
    
    return r;
};
