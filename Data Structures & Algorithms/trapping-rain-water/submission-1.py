class Solution:
    def trap(self, height: List[int]) -> int:
        preMax = []
        postMax = []

        for i in range(len(height)):
            if not preMax:
                preMax.append(0)
            else:
                preMax.append(max(height[i-1], preMax[i-1]))

        for i in range(len(height)):
            if not postMax:
                postMax.append(0)
            else:
                postMax.append(max(height[len(height)-i], postMax[i-1]))

        res = 0

        for i in range(len(preMax)):
            waterAmt = min(preMax[i], postMax[len(postMax)-1-i]) - height[i]
            if waterAmt > 0:
                res += waterAmt
        
        return res