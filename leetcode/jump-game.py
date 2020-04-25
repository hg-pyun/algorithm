class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastPos = len(nums) - 1
        for i in range(lastPos, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i

        return lastPos == 0
