# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def binarySearch(self, binaryMatrix, current_col, size):
        lo = 0
        hi = size - 1
        
        while lo < hi:
            m = math.floor((lo + hi)/2)
            if binaryMatrix.get(current_col, m) == 1:
                hi = m
            else:
                lo = m + 1
        
        if lo == hi and binaryMatrix.get(current_col, lo) == 0:
            return math.inf
        else:
            return lo
        
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        [col_len, row_len] = binaryMatrix.dimensions()

        result = math.inf
        for i in range(col_len):
            left_most = self.binarySearch(binaryMatrix, i, row_len)
            result = min(result, left_most)
            
        return result if result is not math.inf else -1
