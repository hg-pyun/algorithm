/**
 * @param {number} num
 * @return {number}
 */
var numberOfSteps  = function(num) {
    return recur(num, 0);
};

function recur(num, step) {
    if(num === 0) return step;
    
    return num % 2 === 0 ? recur(num / 2, ++step) : recur(num - 1, ++step);
}
