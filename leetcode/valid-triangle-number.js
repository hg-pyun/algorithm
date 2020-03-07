/**
 * @param {number[]} nums
 * @return {number}
 */
var triangleNumber = function(nums) {
    
    nums.sort((a, b) => a - b);
    
    let count = 0;
    for(let i = 0; i < nums.length - 2; i++) {
        for(let j = i + 1; j < nums.length - 1; j++) {
            for(let k = j + 1; k < nums.length; k++) {
                if(checkTriangle([nums[i], nums[j], nums[k]])) {
                    count++;
                }
            }
        }
    }
    
    return count;
};

function checkTriangle(inputs) {
    return inputs[0] + inputs[1] > inputs[2];
}
