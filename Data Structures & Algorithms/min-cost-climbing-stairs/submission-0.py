class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        track = [0, 0]
        for i in range(2, len(cost)):
            track.append(min(cost[i - 2] + track[i - 2], cost[i - 1] + track[i - 1]))
        return min(cost[-2] + track[-2], cost[-1] + track[-1])