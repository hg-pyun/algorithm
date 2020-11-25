class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dest = {}
        
        for [a, b] in paths:
            dest[a] = b
            
            
        p = paths[0][0]
        
        while True:
            if p in dest:
                p = dest[p]
            else:
                break
                
        return p
