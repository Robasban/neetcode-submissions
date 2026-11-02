class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        res = [-1] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                res[coin] = 1
        
        print(res)

        for i in range(1, amount + 1):
            if res[i] == -1:
                lowest = float('inf')
                for c in coins:
                    if i - c > 0 and res[i - c] != -1:
                        lowest = min(res[i - c], lowest)
                if lowest != float('inf'):
                    res[i] = lowest + 1

        return res[-1]