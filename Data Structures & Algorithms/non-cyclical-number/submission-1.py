class Solution:
    def isHappy(self, n: int) -> bool:
        track = set()
        while n not in track:
            if n == 1:
                return True
            track.add(n)
            total = 0
            while n > 0:
                total += (n % 10) ** 2
                n //= 10
            n = total
        
        return False