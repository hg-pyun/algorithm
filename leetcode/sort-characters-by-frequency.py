class Solution:
    def frequencySort(self, s: str) -> str:
        f_map = {}
        
        for c in s:
            if c in f_map:
                f_map[c] += 1
            else:
                f_map[c] = 1
        
        t = sorted(f_map.items(), key=operator.itemgetter(1), reverse=True)
        r = ''
        
        for (c, fq) in t:
            for _ in range(fq):
                r += c
        
        return r
