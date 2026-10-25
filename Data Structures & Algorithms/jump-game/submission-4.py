class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = nums[0]
        i = 0
        while jumps > 0 and i < len(nums) - 1:
            i += 1
            jumps -= 1
            jumps = max(jumps, nums[i])
        
        return i == len(nums) - 1