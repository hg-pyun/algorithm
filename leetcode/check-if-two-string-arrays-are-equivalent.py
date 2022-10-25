class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return self.join(word1) == self.join(word2)
    
    def join(self, words):
        w = ""
        
        for word in words:
            w += word
        
        return w
