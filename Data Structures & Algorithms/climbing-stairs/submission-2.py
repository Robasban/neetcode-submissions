class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        track = [1, 2]
        for i in range(2, n):
            track.append(track[i - 1] + track[i - 2])
        return track[-1]