class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = "0" + text1
        text2 = "0" + text2
        
        text1_len = len(text1)
        text2_len = len(text2)
        
        dp = [[0 for i in range(text1_len)] for j in range(text2_len)]
        
        for i in range(text1_len):
            for j in range(text2_len):
                if i == 0 or j == 0:
                    continue
                
                if text1[i] == text2[j]:
                    dp[j][i] = dp[j - 1][i - 1] + 1
                else:
                    dp[j][i] = max(dp[j - 1][i], dp[j][i - 1])
        
        return dp[text2_len - 1][text1_len - 1]
