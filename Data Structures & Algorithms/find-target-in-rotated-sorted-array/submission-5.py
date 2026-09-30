class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            if nums[m] == target:
                return m
            
            if nums[l] > nums[m] and nums[l] > target and nums[r] > target:
                r = m - 1
            elif nums[l] < target and target < nums[m]:
                r = m - 1
            elif nums[l] < target and nums[m] < target and nums[l] > nums[m]:
                r = m - 1
            else:
                l = m + 1

        return -1