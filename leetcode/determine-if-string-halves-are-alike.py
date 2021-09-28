class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        half = len(s) // 2
        a = s[:half]
        b = s[half:]
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        a_count = 0
        b_count = 0
        
        for char in a:
            if char in vowels:
                a_count += 1
        
        for char in b:
            if char in vowels:
                b_count += 1
                
        return a_count == b_count
