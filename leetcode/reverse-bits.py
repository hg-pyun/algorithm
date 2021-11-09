class Solution:
    def reverseBits(self, n: int) -> int:
       
        string_n = "{0:b}".format(n)
        
        pad = ""
        pad_count = 32 - len(string_n)
        
        for _ in range(pad_count):
            pad += "0"
    
        string_n = pad + string_n
        ans = 0
         
        for i in range(len(string_n)):
            ans += int(string_n[i]) * (2**i)
                
        return ans
