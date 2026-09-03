class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        numSet = set(nums)

        maxTotal = 1

        for i in range(len(nums)):
            if nums[i] + 1 in numSet:
                continue
            tempTotal = 1
            prev = nums[i] - 1
            while prev in numSet:
                tempTotal += 1
                prev -= 1

            maxTotal = max(maxTotal, tempTotal)

        return maxTotal
