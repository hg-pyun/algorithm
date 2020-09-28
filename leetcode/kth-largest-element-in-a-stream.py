class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.sorted_nums = sorted(nums, reverse=True)
        

    def add(self, val: int) -> int:
        self.sorted_nums.append(val)
        self.sorted_nums = sorted(self.sorted_nums, reverse=True)
        
        return self.sorted_nums[self.k - 1]
        

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
