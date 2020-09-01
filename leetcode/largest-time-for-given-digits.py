import copy

class Solution:
    
    def validate(self, c):
        hour = c[0:2]
        minute = c[2:4]
        
        if int(hour) > 23 or int(minute) > 59:
            return False
        else:
            return True
        
    def largestTimeFromDigits(self, A: List[int]) -> str:
        
        candidate = []
        
        def dfs(dep, r, A):
            if dep < 0:
                nonlocal candidate
                candidate.append(r)
                return
            
            for i in range(dep + 1):
                copy_list = copy.deepcopy(A)
                del copy_list[i]
                dfs(dep - 1, r + str(A[i]), copy_list)
        
        dfs(3, "", A)
        
        candidate = set(candidate)
        
        filtered = []
        
        for c in candidate:
            if self.validate(c):
                filtered.append(c)
                
        if not filtered:
            return ''
        
        m = '0000'
        for i in range(len(filtered)):
            cur = filtered[i]
            cur_hour = int(str(cur[0:2]))
            cur_minute = int(str(cur[2:4]))
            
            m_hour = int(str(m[0:2]))
            m_minute = int(str(m[2:4]))
            
            if cur_hour > m_hour:
                m = cur
            elif cur_hour == m_hour:
                if cur_minute > m_minute:
                    m = cur
                    
        return m[0:2] + ':' + m[2:4]
