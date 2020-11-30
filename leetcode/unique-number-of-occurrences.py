class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = [0 for i in range(2001)]
        for n in arr:
            counter[n] += 1
        m = {}
        for n in counter:
            if n == 0:
                continue
            if n in m:
                return False
            else:
                m[n] = 1
        return True
