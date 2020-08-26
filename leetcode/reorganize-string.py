class Solution:
    def reorganizeString(self, S: str) -> str:
        M = {}
        
        for s in S:
            if s in M:
                M[s] += 1
            else:
                M[s] = 1
        
        largest_key = None
        largest_frq = 0
        
        for key in M:
            if M[key] > largest_frq:
                largest_key = key
                largest_frq = M[key]
        
        remain_frq = 0
        
        for key in M:
            if key is not largest_key:
                remain_frq += M[key]
        
        r = ""
        
        if largest_frq > remain_frq + 1:
            return r
        
        count = largest_frq + remain_frq

        last_key = None
        def getLargestFrqWord():
            lk = None
            lfrq = 0
            for key in M:
                if M[key] > lfrq and key != last_key:
                    lk = key
                    lfrq = M[key]
            M[lk] -= 1        
            return lk
        
        while count > 0:
            largest_frq_word = getLargestFrqWord()
            r += largest_frq_word
            last_key = largest_frq_word
            count -= 1
        
        return r
