class Solution:
    def binaryGap(self, n: int) -> int:

        binary = ""
        
        while n > 0:
            binary += str(n % 2)
            n = n // 2

        ans = 0
        counter = 0
        check = False

        for i in range(len(binary)):
            if binary[i] == "1" and check:
                check = False
                ans = max(ans, counter + 1)
                counter = 0

            if check:
                counter += 1

            if binary[i] == "1" and check == False:
                check = True
        
        return ans
