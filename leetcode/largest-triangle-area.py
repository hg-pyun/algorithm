class Solution:
    def get_triangle_area(self, p1, p2, p3):
        first = (p1[0] * p2[1]) + (p2[0] * p3[1]) + (p3[0] * p1[1])
        second = (p1[1] * p2[0]) + (p2[1] * p3[0]) + (p3[1] * p1[0])
        
        re = (first - second) * 0.5
        if re >= 0:
            return re
        else:
            return re * - 1
        
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        
        length = len(points)
        
        ans = 0
        
        for i in range(length):
            for j in range(i + 1, length):
                for k in range(j + 1, length):
                    ans = max(ans, self.get_triangle_area(points[i], points[j], points[k]))
        
        return ans
