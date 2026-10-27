class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        for trip in triplets:
            if trip[0] <= target[0] and trip[1] <= target[1] and trip[2] <= target[2]:
                max1 = max(max1, trip[0])
                max2 = max(max2, trip[1])
                max3 = max(max3, trip[2])
        
        return [max1, max2, max3] == target