/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    for(let i = 0; i < nums.length; i++) {
        for(let j = 0; j < nums.length - 1; j++) {
            if(nums[j] === 0) {
                const temp = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = temp;
            }
        }
    }
};

// A better solution

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    
    let idx = 0
    
    for(let i=0; i< nums.length; i++) {
        let curr = nums[i]
        if(curr !== 0) {
            nums[idx] = curr
            idx++
        }
    }
    
    for(let j=idx; j < nums.length; j++) {
        nums[j] = 0
    }
    return nums
};
