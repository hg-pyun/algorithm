class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        if digits == "":
            return []
        
        m = {
            '2': ['a','b','c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        
        ans = []
        
        def dfs(str_list, joined, index):
            if index == len(str_list):
                ans.append(joined)
                return
            
            char_set = m[str_list[index]]
            
            for char in char_set:
                dfs(str_list, joined + char, index + 1)

        digits_list = list(digits)
        dfs(digits_list, "", 0)
        
        return ans
