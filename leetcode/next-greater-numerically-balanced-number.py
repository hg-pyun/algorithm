class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        
        candidate = n + 1
        
        while (True):
            string_n = str(candidate)
            
            checker = {};
            for digit in string_n:
                if digit in checker:
                    checker[digit] += 1
                else:
                    checker[digit] = 1
            
            find = True
            for key in checker:
                if checker[key] != int(key):
                    find = False
                    break;
            
            if find:
                break;
            else:
                candidate += 1
            
        return candidate
