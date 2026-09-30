class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices) - 1

        res = 0

        while l < r:
            res = max(res, prices[r] - prices[l])
            if prices[l] > prices[l + 1]:
                l += 1
            elif prices[r] < prices[r - 1]:
                r -= 1
            else:
                l += 1

        return max(res, 0)