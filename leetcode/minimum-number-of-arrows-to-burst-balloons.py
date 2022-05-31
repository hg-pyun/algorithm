class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sorted_points = sorted(points)
        length = len(sorted_points)
        
        prev = sorted_points[0]
        removed = 0
        
        for i in range(1, length):
            current = sorted_points[i]
            
            if prev[1] >= current[0]:
                removed += 1
                if prev[1] > current[1]:
                    prev = current
            else:
                prev = current
            
        return length - removed
