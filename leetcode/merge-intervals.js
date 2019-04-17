/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
var merge = function(intervals) {

    const stack = [];
    
    intervals.sort((a, b)=> {
        return a[0] - b[0];
    });
    
    for(let i=0; i<intervals.length; i++) {
        
        if(stack.length === 0) {
            stack.push(intervals[i]);
        }
        else {
            const before = stack.pop();
            
            const beforeS = before[0];
            const beforeE = before[1];
            const currentS = intervals[i][0];
            const currentE = intervals[i][1];

            if(beforeS <= currentS && beforeE >= currentE) {
                stack.push([beforeS, beforeE]);
            } 
            else if(beforeE >= currentS) {
                stack.push([beforeS, currentE]);
            }
            else {
                stack.push(before);
                stack.push(intervals[i]);
            }
        }
    }
    
    return stack;
};
