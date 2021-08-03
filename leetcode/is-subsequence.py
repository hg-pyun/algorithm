class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # filter edge case
        if s == "":
            return True
             
        p = 0;
        
        for cur_str in t:
            # check finished
            if p == len(s):
                return True
            
            if cur_str == s[p]:
                p += 1
        
        return p == len(s)
