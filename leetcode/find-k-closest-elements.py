class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        diff = []
        
        for i in range(len(arr)):
            diff.append((abs(arr[i] - x), i))
        
        diff = sorted(diff, reverse=True)
        
        ans = []
        for i in range(k):
            ans.append(arr[diff.pop()[1]])
        
        return sorted(ans)
