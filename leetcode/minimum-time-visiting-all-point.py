class Solution:
    def distance(self, p1, p2):
        diff_x = abs(p1[0] - p2[0])
        diff_y = abs(p1[1] - p2[1])
        
        return max(diff_x, diff_y)
        
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        
        for i in range(len(points) - 1):
            ans += self.distance(points[i], points[i+1])
        
        return ans
