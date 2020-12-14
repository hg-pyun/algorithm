class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        m = {}
        
        for n in arr:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1
        
        for n in arr:
            if n * 2 in m and n is not 0:
                return True
            elif n is 0 and m[n] == 2:
                return True
            
        return False
