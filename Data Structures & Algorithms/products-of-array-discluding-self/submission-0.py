class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroIndex = -1
        prodTotal = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                if zeroIndex != -1:
                    return [0] * len(nums)
                else:
                    zeroIndex = i
            else:
                prodTotal *= nums[i]
        
        if zeroIndex != -1:
            res = [0] * len(nums)
            res[zeroIndex] = prodTotal
            return res
        
        res = [prodTotal] * len(nums)

        for i in range(len(nums)):
            res[i] //= nums[i]

        return res