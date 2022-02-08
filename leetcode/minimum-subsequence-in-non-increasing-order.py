class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums, reverse = True)
        
        total = reduce(lambda acc, cur: acc+ cur, sorted_nums, 0)
        acc = 0
        ans = []
        
        for num in sorted_nums:
            ans.append(num)
            
            acc += num
            total -= num
            
            if acc > total:
                return ans
