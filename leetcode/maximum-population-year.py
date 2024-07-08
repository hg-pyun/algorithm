class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:        
        histogram = [0 for _ in range(100)]

        for [b, d] in logs:
            for i in range(b, d):
                histogram[i - 1950] += 1
        
        index = 99
        result = 0
        for i in range(99, -1, -1):
            print(i, result, histogram[i])
            if result <= histogram[i]:
                result = histogram[i]
                index = i

        return 1950 + index
