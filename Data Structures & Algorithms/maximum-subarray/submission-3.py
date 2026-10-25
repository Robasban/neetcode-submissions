class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = total = nums[0]

        for i in range(1, len(nums)):
            total += nums[i]
            if total < nums[i]:
                total = nums[i]
            elif total < 0:
                total = 0
            res = max(res, total)

        return res