class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        subset = []

        def backtrack(index, total):
            if total > target:
                return

            if total == target:
                res.append(subset.copy())
                return

            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                subset.append(candidates[i])
                backtrack(i + 1, total + candidates[i])
                subset.pop()

        backtrack(0, 0)

        return res
