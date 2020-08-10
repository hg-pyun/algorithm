class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        cache = {}
        
        for el in A:
            if el in cache:
                return el
            else:
                cache[el] = 1
