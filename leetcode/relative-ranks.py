class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        m = dict()
        
        sorted_score = sorted(score, reverse=True)
        
        for i in range(len(sorted_score)):
            if i == 0:
                m[sorted_score[i]] = "Gold Medal"
            elif i == 1:
                m[sorted_score[i]] = "Silver Medal"
            elif i== 2:
                m[sorted_score[i]] = "Bronze Medal"
            else:
                m[sorted_score[i]] = str(i + 1)
        
        ans = []
        
        for num in score:
            ans.append(m[num])
        
        return ans
