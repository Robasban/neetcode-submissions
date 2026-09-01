class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        if len(count) == 1:
            return list(count.keys())

        countList = [[] for i in range(len(nums))]
        
        for key in count.keys():
            countList[count[key]] += [key]

        kList = []

        for i in range(len(nums)):
            kList += countList[len(nums) - 1 - i]
            if len(kList) == k:
                return kList