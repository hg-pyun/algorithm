class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        count = 0
        p = 0
        for i in range(1, 2001):
            if p >= len(arr):
                count += 1
            else:
                if i == arr[p]:
                    p += 1
                else:
                    count += 1
            
            if count == k:
                return i
