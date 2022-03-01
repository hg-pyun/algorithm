class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        ans = []
        carry = False
        
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9 and i == len(digits) - 1:
                ans.insert(0, 0)
                carry = True
            else:
                if carry:
                    if digits[i] == 9:
                        ans.insert(0, 0)
                    else:
                        ans.insert(0, digits[i] + 1)
                        carry = False
                else:
                    if i == len(digits) - 1:
                        ans.insert(0, digits[i] + 1)
                    else:
                        ans.insert(0, digits[i])
                    carry = False
    
        if carry:
            ans.insert(0, 1)
            
        return ans
