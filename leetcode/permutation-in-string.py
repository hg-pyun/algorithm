class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        def match(a1, a2):
            for i in range(26):
                if a1[i] != a2[i]:
                    return False
            return True
        
        record = [0 for i in range(26)]
        
        for c in s1:
            record[ord(c) - 97] += 1
        
        for i in range(len(s2) - len(s1) + 1):
            check = [0 for i in range(26)]
            
            for j in range(len(s1)):
                check[ord(s2[i + j]) - 97] += 1
            
            if match(record, check):
                return True
                
        return False
