class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        jumps = 0
        while i < len(nums) - 1:
            if nums[i] > jumps:
                jumps = nums[i]
            if jumps == 0:
                return False
            i += 1
            jumps -= 1
    
        return True
