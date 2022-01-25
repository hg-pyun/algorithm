class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        candidate = [i for i in range(0, len(s) + 1)]
        
        ans = []
        for char in s:
            if char == 'I':
                ans.append(candidate.pop(0))
            else:
                ans.append(candidate.pop())
        
        ans.append(candidate.pop())
        
        return ans
