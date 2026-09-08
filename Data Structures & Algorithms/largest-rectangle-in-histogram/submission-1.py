class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxHeight = 0

        res = []

        for i in range(len(heights)):
            indexBack = 0
            while res and heights[i] < res[-1][0]:
                vals = res.pop()
                maxHeight = max(maxHeight, vals[0] * (i - vals[1]))
                indexBack = i - vals[1]
            res.append((heights[i], i - indexBack))

        while res:
            vals = res.pop()
            maxHeight = max(maxHeight, vals[0] * (len(heights) - vals[1]))

        return maxHeight