class Solution:
    def specialArray(self, nums: List[int]) -> int:
        
        check = [-1 for _ in range(1000)]
        
        for num in nums:
            for i in range(0, num):
                check[i] += 1
        
        for i in range(len(check)):
            if i == check[i]:
                return check[i] + 1
        
        return -1
