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
    
    def isSameParent(self, x, y):
        x = self.find(x)
        y = self.find(y)
        return x == y
        
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        for i in range(n):
            self.p.append(i)
        
        remain_cable = 0
        
        for [x, y] in connections:
            if self.isSameParent(x, y):
                remain_cable += 1
            else:
                self.union(x, y)
                
        s = set()
        for i in range(n):
            s.add(self.find(i))

        remain_con = len(s) - 1
        
        if remain_con < 0:
            return 0
        elif remain_cable < remain_con:
            return -1
        else:
            return remain_con
            
