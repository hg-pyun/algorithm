class Solution:
    def customSortString(self, order: str, s: str) -> str:
        s_list = list(s)
        
        length = len(s_list)
        for i in range(length):
            for j in range(0, length-i-1):
                if order.find(s_list[j]) > order.find(s_list[j+1]):
                    s_list[j], s_list[j+1] = s_list[j+1], s_list[j]
        
        return ''.join(s_list)
      
