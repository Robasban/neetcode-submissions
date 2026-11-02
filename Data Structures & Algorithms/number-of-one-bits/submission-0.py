class Solution:
    def hammingWeight(self, n: int) -> int:
        mult = 1
        while mult < n:
            mult *= 2
        
        res = 0

        while n > 0:
            if mult <= n:
                n -= mult
                res += 1
            mult /= 2
        
        return res