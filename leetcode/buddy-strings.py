class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        l = len(s)
        letter_s = [0 for _ in range(26)]
        letter_goal = [0 for _ in range(26)]
        
        ti = 0
        tj = 0
        count = 0;
        duplicated = False;
        for i in range(l):
            if s[i] != goal[i]:
                if count == 0:
                    ti = i
                else:
                    tj = i
                count += 1;
                
            letter_s[ord(s[i]) - ord('a')] += 1
            letter_goal[ord(goal[i]) - ord('a')] += 1
        
        if len(s) != len(goal):
            return False
        
        for i in range(26):
            if letter_s[i] >= 2:
                duplicated = True
            if letter_s[i] != letter_goal[i]:
                return False
            
        if count > 2:
            return False
        
        if s == goal and duplicated:
            return True
        
        if ti != tj:
            return True
        
        return False
