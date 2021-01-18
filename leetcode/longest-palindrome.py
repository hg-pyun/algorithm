class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        m = {}
        
        for c in s:
            if c in m:
                m[c] += 1
            else:
                m[c] = 1

        ans = 0
        longest_odd = 0
        longest_char = None;
        
        for key in m:
            if m[key] % 2 == 1:
                if longest_odd < m[key]:
                    longest_char = key
            else:
                ans += m[key]
                
        for key in m:
            if m[key] % 2 == 1:
                if key == longest_char:
                    ans += m[key]
                else:
                    ans += m[key] - 1
        
        return ans
