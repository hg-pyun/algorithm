class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix) # col
        n = len(matrix[0]) # row
        
        result = []
        for i in range(m):
            [min_index, min_val] = self.find_min(matrix[i], n)
            if self.check_col(matrix, min_index, min_val):
                result.append(min_val)
            
        
        return result
     
    def find_min (self, row, length):
        min_val = math.inf
        min_index = math.inf
        
        for i in range(length):
            if row[i] < min_val:
                min_val = row[i]
                min_index = i
            
        return [min_index, min_val]
    
    def check_col (self, matrix, col, candidate):
        isLucky = True
        
        for i in range(len(matrix)):
            if candidate < matrix[i][col]:
                isLucky = False
        
        return isLucky
