import heapq

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        hq = []

        for num in nums:
            heapq.heappush(hq, -int(num))

        ans = ""

        for i in range(k):
            ans = heapq.heappop(hq)

        return str(abs(ans))
