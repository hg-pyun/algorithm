class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        
        table = {}
        
        alphabets = list(map(chr, range(97, 123)))
        alphabets_ptr = 0
                        
        for char in key:
            if char in table or char == ' ':
                continue;
            else:
                table[char] = alphabets[alphabets_ptr]
                alphabets_ptr += 1
        
        ans = '';
        
        for char in message:
            if char == ' ':
                ans += ' ';
            else:
                ans += table[char]
        
        return ans
