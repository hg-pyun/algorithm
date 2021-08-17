class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u'];
        
        ans = []
        a = 'a';
        for word in sentence.split():
            if word[0].lower() in vowel:
                ans.append(word + 'ma' + a)
                
            else:
                ans.append(word[1:] + word[0] + 'ma' + a)
            
            a += 'a'
        
        return " ".join(ans)
