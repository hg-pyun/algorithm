/**
 * @param {string} S
 * @param {number} K
 * @return {string}
 */
var licenseKeyFormatting = function(S, K) {
    
    const r = [];
    
    let assembler = [];
    let count = 0;
    
    for(let i = S.length - 1; i >= 0; i--) {
        const char = S[i];
             
        if(char !== '-') {
            assembler.push(char);
            count++;   
        }
        
        if(count >= K || i === 0) {
            assembler.length > 0 && r.push(assembler.reverse().join(''));
            count = 0;
            assembler = [];
        }
    }
    
    return r.reverse().join('-').toUpperCase();
};
