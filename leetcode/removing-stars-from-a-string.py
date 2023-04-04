class Solution:
    def removeStars(self, s: str) -> str:

        ans = ''
        skip = 0

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '*':
                skip += 1
            else:
                if skip:
                    skip -= 1
                else:
                    ans += s[i]
        
        return ans[::-1]
