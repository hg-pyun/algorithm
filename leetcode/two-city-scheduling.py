from functools import cmp_to_key

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        def compare(x, y):
            return abs(x[0] - x[1]) - abs(y[0] - y[1])
            
        costs = sorted(costs, key=cmp_to_key(compare), reverse=True)
        
        a = 0
        b = 0
        r = 0
        for cost in costs:
            if a >= len(costs)/2:
                b += 1
                r += cost[1]
                continue
            
            elif b >= len(costs)/2:
                a += 1
                r += cost[0]
                continue
            
            if cost[0] < cost[1]:
                a += 1
                r += cost[0]
            else:
                b += 1
                r += cost[1]
        
        return r
