class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        left = []
        right = []
        center = []
        
        for i in range(len(nums)):
            if nums[i] < pivot:
                left.append(nums[i])
            elif nums[i] > pivot:
                right.append(nums[i])
            else:
                center.append(nums[i])
                
        return left + center + right
