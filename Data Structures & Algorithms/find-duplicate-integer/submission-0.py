class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        track = set()
        for num in nums:
            if num in track:
                return num
            else:
                track.add(num)