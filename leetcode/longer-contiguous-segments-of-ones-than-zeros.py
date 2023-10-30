class Solution:
    def checkZeroOnes(self, s: str) -> bool:

        length_0 = 0
        length_1 = 0

        check_0 = False
        check_1 = False

        count_0 = 0
        count_1 = 0

        for char in s:
            if char == "0":
                count_0 += 1

            if char == "0" and not check_0:
                check_0 = True
            elif char == "1" and check_0:
                check_0 = False
                length_0 = max(count_0, length_0)
                count_0 = 0

            if char == "1":
                count_1 += 1
            
            if char == "1" and not check_1:
                check_1 = True
            elif char == "0" and check_1:
                check_1 = False
                length_1 = max(count_1, length_1)
                count_1 = 0
        

        length_0 = max(count_0, length_0)
        length_1 = max(count_1, length_1)
        
        return length_1 > length_0
