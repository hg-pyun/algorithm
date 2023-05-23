class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        map = {}

        for char in s:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1
        
        for char in t:
            if char in map:
                if map[char] == 0:
                    return char
                else:
                    map[char] -= 1
            else:
                return char
