/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var combinationSum4 = function(nums, target) {
    const dp = [..._.range(0, 1000)].map(x => -1);
    return dfs(nums, target, dp)
};

function dfs(nums, target, dp) {
    if (target === 0) return 1;
    if (dp[target] !== -1) return dp[target];

    dp[target] = 0;

    for (let num of nums) {
        if(num <= target) {
            dp[target] += dfs(nums, target - num, dp);
        }
    }

    return dp[target]
}
