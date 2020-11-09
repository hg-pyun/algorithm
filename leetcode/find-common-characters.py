class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        ans = []
        count = [[0 for i in range(26)] for i in range(len(A))]
        
        for i in range(len(A)):
            for char in A[i]:
                count[i][ord(char) - ord('a')] += 1
        
        merge = [101 for i in range(26)]
        for i in range(len(A)):
            for j in range(26):
                merge[j] = min(count[i][j], merge[j])
        
        for i in range(26):
            for _ in range(merge[i]):
                ans.append(chr(i + ord('a')))
        return ans
