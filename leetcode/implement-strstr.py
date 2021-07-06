class Solution:
    def check(self, i, haystack, needle):
        for j in range(len(needle)):
            if haystack[i] != needle[j]:
                return False
            i += 1
        return True
        
    def strStr(self, haystack: str, needle: str) -> int:
    
        len_haystack = len(haystack)
        len_needle = len(needle)
        
        if len_needle == 0 or haystack == needle:
            return 0
        
        if len_haystack == 0 or len_haystack < len_needle:
            return -1
        
        target = -1
        
        for i in range(len_haystack):
            if haystack[i] == needle[0] and len_haystack - i >= len_needle:
                if self.check(i, haystack, needle):
                    target = i;
                    break;
                
        return target
