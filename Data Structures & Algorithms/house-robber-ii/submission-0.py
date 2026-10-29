class Solution:
    def rob(self, nums: List[int]) -> int:

        res = 0

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def dp(i, j):
            prev2 = nums[i]
            prev1 = max(nums[i], nums[i + 1])
            i += 2
            while i < j:
                temp = max(nums[i] + prev2, prev1)
                prev2 = prev1
                prev1 = temp
                i += 1
            
            return prev1

        res = dp(1, len(nums))
        res = max(res, dp(0, len(nums) - 1))

        return res