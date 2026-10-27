class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        subset = []

        def backtrack(total):
            if total > target:
                return
            elif total == target:
                res.append(subset.copy())
                return
            for num in nums:
                if subset and num > subset[-1]:
                    continue
                subset.append(num)
                total += num
                backtrack(total)
                total -= num
                subset.pop()
        
        backtrack(0)

        return res



