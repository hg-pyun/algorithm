class Solution:
    def getLucky(self, s: str, k: int) -> int:
        
        num_string =""
        
        for char in s:
            num_string += str(ord(char) - 96)
        
        while k > 0:
            temp = 0
            for char in num_string:
                temp += int(char)
            
            num_string = str(temp)
            k -= 1
            
        return num_string
