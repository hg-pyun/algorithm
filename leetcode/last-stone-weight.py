class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        
        while len(stones) > 1:
            first = stones.pop()
            second = stones.pop()
        
            if first == second:
                continue
            else:
                diff = first - second

                done = True
                for i in range(len(stones)):
                    if diff <= stones[i]:
                        stones.insert(i, diff)
                        done = False
                        break
                if done:
                    stones.append(diff)
                              
        return len(stones) == 1 and stones[0] or 0
