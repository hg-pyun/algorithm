class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        
        count = {}
        
        for [id, time] in logs:
            if id in count:
                count[id].add(time)
            else:
                count[id] = set([time])
            
        
        ans = [0 for i in range(k)]
        
        # 유니크한 액션의 갯수를 배열에 기록
        for key in count:
            ans[len(count[key]) - 1] += 1
            
        return ans
            
