class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        checker = {}
        
        for char in ransomNote:
            if char in checker:
                checker[char] += 1
            else:
                checker[char] = 1

        for char in magazine:
            if char in checker:
                checker[char] -= 1
        
        for v in checker.values():
            if v > 0:
                return False
        
        return True
