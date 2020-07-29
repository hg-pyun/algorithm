import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        bucket = {}
        for num in nums:
            if num in bucket:
                bucket[num] += 1
            else:
                bucket[num] = 1

        heap = []
        for key in bucket:
            heapq.heappush(heap, (-bucket[key], key))
         
        r = []
        for i in range(k):
            r.append(heapq.heappop(heap)[1])
            
        return r
