class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def checkPalindrome(word):
            l = len(word)
            for i in range(l // 2):
                last = l - 1 - i
                
                if word[i] != word[last]:
                    return False
                
            return True
        
        for word in words:
            if checkPalindrome(word):
                return word
        
        return ""
