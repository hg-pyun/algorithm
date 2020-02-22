/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    const result = [];
    
    let assembler = [];
    
    function dfs(s, step) {
        if(step === 4)
            return s.length === 0 && result.push(assembler.join('.'));
    
        for(let i = 1; i < 4; ++i) {
            const adr = s.slice(0, i);
            const remain = s.slice(i, s.length);
            
            if(/^0.+/.test(adr) || Number(adr) > 255 || i > s.length) break;
            
            assembler.push(adr);
            dfs(remain, step + 1);
            assembler.pop();
        }
    }
    
    dfs(s, 0);
    
    return result;
};
