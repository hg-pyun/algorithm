class Solution:
    
    def search_negative_pos(self, arr):
        l = 0
        r = len(arr)
        mid = -1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < 0:
                r = mid        
            else:
                l = mid + 1
        
        return l
    
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans = 0
        l = len(grid[0])
        for row in grid:
            print(self.search_negative_pos(row))
            ans += l - self.search_negative_pos(row)
        
        return ans
