class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)

        l, r = 1, maxPile

        k = 0

        while l < r:
            k = (l + r) // 2

            totalHours = 0
            for i in range(len(piles)):
                totalHours += math.ceil(piles[i] / k)

            if totalHours > h:
                l = k + 1
            else:
                r = k
        
        return k + 1