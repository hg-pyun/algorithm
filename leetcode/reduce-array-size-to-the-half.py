class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        
        m = {}
        
        for n in arr:
            if n in m:
                m[n] += 1
            else:
                m[n] = 1
        
        sorted_m = {k: v for k, v in sorted(m.items(), key=lambda item: item[1], reverse=True)}
        
        ans = 0
        length = len(arr)
        
        for key in sorted_m:
            ans += 1
            length -= sorted_m[key]
            
            if length <= len(arr) // 2:
                break
        
        return ans
