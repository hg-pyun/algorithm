class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        checker = {}
        
        for char in s:
            if char in checker:
                checker[char] += 1
            else:
                checker[char] = 1

        for char in t:
            if char in checker:
                checker[char] -= 1
        
        for v in checker.values():
            if v > 0:
                return False
        
        return True
