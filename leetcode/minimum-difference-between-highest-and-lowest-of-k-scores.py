class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        length = len(nums)
        sorted_nums = sorted(nums)

        diff = []
        for i in range(length - 1):
            diff.append(sorted_nums[i+1] - sorted_nums[i])

        target = sum(diff[0:k-1])
        ans = target
        window_size = k - 1

        for i in range(0, len(diff) - k + 1):
            target -= diff[i]
            target += diff[i + window_size]
            ans = min(ans, target)

        return ans
