class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxPile = max(piles)

        l, r = 1, maxPile

        k = (l + r) // 2

        while l < r:

            totalHours = 0
            for i in range(len(piles)):
                totalHours += math.ceil(piles[i] / k)

            if totalHours > h:
                l = k + 1
            else:
                r = k

            k = (l + r) // 2
        
        return k