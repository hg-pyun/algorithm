class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
                
        length = len(gas)
        ans = -1
        
        for position in range(length):
            cursor = position
            tank = gas[position]
            
            if tank < cost[position]:
                continue
        
            while tank > 0:
                tank -= cost[cursor % length]
                if tank >= 0:
                    cursor += 1
                else:
                    break;
                    
                tank += gas[cursor % length]
                
                if (cursor % length) == position:
                    ans = position
                    return ans
        
        return ans
