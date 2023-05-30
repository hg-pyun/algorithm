class Solution:
    def euclidean(self, a, b):
        while b > 0:
            a, b = b, a % b
        return a
    
    def count_common_factor(self, n):
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += 1
        return count


    def commonFactors(self, a: int, b: int) -> int:

        gcd = self.euclidean(a, b)
        ans = self.count_common_factor(gcd)
        
        return ans
