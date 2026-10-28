class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev2 = 0
        prev1 = 0
        for i in range(2, len(cost)):
            temp = min(cost[i - 2] + prev2, cost[i - 1] + prev1)
            prev2 = prev1
            prev1 = temp
        return min(cost[-2] + prev2, cost[-1] + prev1)