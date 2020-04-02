/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function(n) {
    let isHappy = false;
    const cycleMap = {}
    
    let number = String(n);
    
    while(!cycleMap[number]) { 
        if(number === '1') {
            isHappy = true;
            break;
        }
        
        let add = 0;
        
        for(let i = 0; i < number.length; i++) {
            add += Math.pow(number[i], 2);
        }
        
        cycleMap[number] = 1;
        number = String(add);
    }
    
    return isHappy;
};
