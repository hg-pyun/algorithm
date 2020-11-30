class Solution:
    def countPrimes(self, n: int) -> int:
        
        c = [1, 1] + [0 for i in range(n - 2)]
        
        for i in range(2, int(sqrt(n)) + 1):
            if c[i] == 1:
                continue
            for j in range(2*i, n, i):
                c[j] = 1
                
        prime_count = 0
        
        for isPrime in c:
            if isPrime == 0:
                prime_count += 1
        
        return prime_count
