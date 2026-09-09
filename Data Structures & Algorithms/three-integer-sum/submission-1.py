class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    saveL = nums[l]
                    while l < r and nums[l] == saveL:
                        l += 1
                    saveR = nums[r]
                    while l < r and nums[r] == saveR:
                        r -= 1

        return res