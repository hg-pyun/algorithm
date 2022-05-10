class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        
        p1 = 0
        p2 = len(s) - 1
        
        s = [ch for ch in s]
        
        while p1 < p2:
            if s[p1] in vowels and s[p2] in vowels:
                temp = s[p2]
                s[p2] = s[p1]
                s[p1] = temp
                p1 += 1
                p2 -= 1
            else:
                if s[p1] not in vowels:
                    p1 += 1
                if s[p2] not in vowels:
                    p2 -= 1

        return "".join(s)
