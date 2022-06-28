import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        heights_len = len(heights)
        
        for i in range(1, len(heights)):
            
            diff = heights[i] - heights[i - 1]
            
            if diff < 0:
                continue
                
            heapq.heappush(heap, diff)
            
            if len(heap) > ladders:
                min_diff = heapq.heappop(heap)
                
                if bricks < min_diff:
                    return i - 1
                
                bricks -= min_diff
                
        return heights_len - 1
