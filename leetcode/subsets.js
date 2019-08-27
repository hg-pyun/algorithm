/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var subsets = function(nums) {
    return getSubsets([...new Set(nums)]);
};

function getSubsets(set)  { 
    const result = [];
    const n = set.length; 
    for (let i = 0; i < (1<<n); i++) {
        const subset = [];
        for (let j = 0; j < n; j++)  {
            if ((i & (1 << j)) > 0) {
                subset.push(set[j]);
            }
        }
        result.push(subset);
    } 
    return result;
} 
