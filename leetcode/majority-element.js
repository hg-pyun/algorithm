/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const cache = new Map();
    
    nums.forEach((num) => {
        if(cache.has(num)) {
            cache.set(num, cache.get(num) + 1);
        }
        else {
            cache.set(num, 1);
        }
    });
    
    let max = -1;
    let r = 0;
    for(let [k, v] of cache) {
        if(v > max) {
            r = k;
            max = v;
        }
    }
    
    return r;
};
