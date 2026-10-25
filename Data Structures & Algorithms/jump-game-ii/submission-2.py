class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        maxIndex = nums[0]
        newMax = 0
        jumps = 1
        i = 1
        while i < len(nums):
            if maxIndex >= len(nums) - 1:
                break
            jumps += 1
            while i <= maxIndex:
                newMax = max(newMax, i + nums[i])
                i += 1
            maxIndex = newMax
            newMax = 0

        return jumps