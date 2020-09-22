class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        arr = [0 for _ in range(len(nums))]
        
        for num in nums:
            arr[num - 1] += 1
        
        ans = []
        for i in range(len(arr)):
            if arr[i] == 0:
                ans.append(i + 1)
        
        return ans
