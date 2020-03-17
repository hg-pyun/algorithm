/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    
    let ans = nums[0];
    let subSum = 0;
        
    for(let i=0;i<nums.length;i++) {  
        subSum += nums[i];  
        ans = Math.max(subSum, ans);
        
        if(subSum < 0)
            subSum = 0;
    }
        
    return ans;
};
