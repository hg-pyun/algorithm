class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        integers = {}
        
        for num in nums:
            integer = int(num, 2);
            integers[int(num, 2)] = num;
        
        max_val = -1
        
        for key in integers:
            max_val = max(key, max_val)
                    
        ans = None
        for i in range(max_val):
            if i not in integers:
                ans = str(int(bin(i)[2:])).zfill(len(integers[max_val]))
                break;
            
        if ans is None:
            return ''.rjust(len(integers[max_val]), '1')
        else:
            return ans
