## TLE
import copy

class Solution:
    
    def check_inclination(self, a, b):
        if a[0] == b[0]:
            return 0
        elif a[1] == b[1]:
            return 99999999
        else:
            return (a[0]- b[0]) / (a[1] - b[1])
    
    def maxPoints(self, points: List[List[int]]) -> int:
        
        ans = 0
        length = len(points)
        
        if length == 1:
            return 1
        
        def traversal(target_point, visit, count, prev_inclination):
            for i in range(length):
                if visit[i] == False:
                    visit[i] = True                    
                    inclination = self.check_inclination(target_point, points[i])
                    
                    if prev_inclination == None or inclination == prev_inclination:
                        nonlocal ans
                        next_count = count + 1
                        ans = max(ans, next_count)
                        traversal(points[i], copy.deepcopy(visit), next_count, inclination)
            
        
        for i in range(length):
            visit = [False for _ in range(length)]
            visit[i] = True
            traversal(points[i], copy.deepcopy(visit), 1, None)
            
        return ans
