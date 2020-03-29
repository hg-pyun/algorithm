/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    
    let max = 0;
    let l = 0;
    let r = height.length - 1;
    
    while(l < r) {
        max = Math.max(max, Math.min(height[l], height[r]) * (r - l));
        if(height[l] < height[r]) {
            l++;
        }
        else {
            r--;
        }
    }
        
    return max;
};
