class Solution:
    def __init__(self):
        self.p = {}
        
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
              
    def equationsPossible(self, equations: List[str]) -> bool:
        
        # initialize
        for eq in equations:
            x = eq[0]
            y = eq[3]
            self.p[x] = x
            self.p[y] = y
        
        # union
        for eq in equations:
            x = eq[0]
            y = eq[3]
            same = eq[1] is '='
            if same:
                self.union(x, y)
        
        # check validation
        for eq in equations:
            x = eq[0]
            y = eq[3]
            if eq[1] is '!' and self.isSameParent(x, y):
                return False
                
        return True
