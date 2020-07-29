import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        bucket = {}
        heap = []
        
        for num1 in nums1:
            for num2 in nums2:
                s = num1 + num2
                heapq.heappush(heap, s)
                if s in bucket:
                    bucket[s].append([num1, num2])
                else:
                    bucket[s] = []
                    bucket[s].append([num1, num2])

        result = []
        for i in range(k):
            if heap:
                target = heapq.heappop(heap)
                result.append(bucket[target].pop())
        
        return result
        
