class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:

        counter = [0 for _ in range(0, 1001)]

        for [value, weight] in items1:
            counter[value] = weight

        
        for [value, weight] in items2:
            counter[value] += weight
        
        ans = []

        for i in range(1001):
            if counter[i] != 0:
                ans.append([i , counter[i]])
        
        return ans
         
