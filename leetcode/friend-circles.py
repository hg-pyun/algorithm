class Solution:
    def __init__(self):
        self.p = []
        
    def find(self, x):
        if x == self.p[x]:
            return x
        else:
            p = self.find(self.p[x])
            self.p[x] = p
            return p
        
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if x < y:
                self.p[y] = x
            else: 
                self.p[x] = y
    
    def findCircleNum(self, M: List[List[int]]) -> int:
        size = len(M)
        
        for i in range(size):
            self.p.append(i)                
            
        for i in range(size):
            for j in range(size):
                if i == j:
                    continue
                elif M[i][j] == 1:
                    self.union(i, j)
                    
        s = set()
        for i in range(size):
            s.add(self.find(i))

        return len(s)
