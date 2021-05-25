class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_boxes = sorted(boxTypes, key=itemgetter(1), reverse=True)
        
        ans = 0
        limit = truckSize;
        
        for [number, unit] in sorted_boxes:
            if limit >= 0:
                ans += min(limit, number) * unit
                limit -= number
        
        return ans
