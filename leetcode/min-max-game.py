class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        target = nums
        temp = []
        
        while len(target) != 1:
            count = 0
            for i in range(0, len(target), 2):
                if count % 2 == 0:
                    temp.append(min(target[i], target[i + 1]))
                else:
                    temp.append(max(target[i], target[i + 1]))
                
                count += 1
            
            target = temp
            temp = []
            
        
        return target[0]
