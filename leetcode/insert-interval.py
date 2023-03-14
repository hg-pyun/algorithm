class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        for interval in intervals:
            print(interval, newInterval)
            if newInterval[1] < interval[0]:
                ans.append(newInterval)
                newInterval = interval
            elif newInterval[0] <= interval[1]:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
            else:
                ans.append(interval)
        
        ans.append(newInterval)

        return ans
