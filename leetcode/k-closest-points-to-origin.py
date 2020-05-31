class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        candidate = []
        for i in range(len(points)):
            [x, y] = points[i]
            candidate.append([abs(pow(x, 2)) + abs(pow(y, 2)), i])
        
        candidate.sort(key = lambda x: x[0])
        
        result = []
        for [_, i] in candidate[:K]:
            result.append(points[i])
            
        return result
