class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        checker = {}
        
        for c in s:
            if c in checker:
                checker[c] += 1
            else:
                checker[c] = 1

        first = None
        for k, v in checker.items():
            if v == 1:
                first = k
                break
        
        return s.index(first) if first is not None else -1
