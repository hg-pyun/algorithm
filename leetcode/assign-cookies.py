class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        grids = sorted(g)
        cookies = sorted(s)
        
        ans = 0
        cursor = 0
        
        for cookie in cookies:
            if grids[cursor] <= cookie:
                ans += 1
                cursor += 1;
            
            if cursor == len(grids):
                break;
                
        return ans
