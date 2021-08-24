class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        
        exclude = 0
        
        for x in arr1:
            for y in arr2:
                if abs(x - y) <= d:
                    exclude += 1
                    break;
        
        return len(arr1) - exclude
