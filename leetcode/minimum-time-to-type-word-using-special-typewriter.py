class Solution:
    def minTimeToType(self, word: str) -> int:
        
        count = 0
        prev = 'a'
        
        for char in word:
            clockwise = abs(ord(char) - ord(prev));
            counterclockwise = abs(clockwise - 26)
            count += min(clockwise, counterclockwise)
            prev = char
        
        return count + len(word)
