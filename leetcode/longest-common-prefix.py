class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        len_min = 201
        
        for s in strs:
            len_min = min(len(s), len_min)
        
        ans = ''
        
        for i in range(len_min):
            done = False
            diff = None
            
            for s in strs:
                if diff == None:
                    diff = s[i]
                elif diff != s[i]:
                    done = True
                    break;
                    
            if done:
                break;
            else:
                ans += diff    
        
        return ans
