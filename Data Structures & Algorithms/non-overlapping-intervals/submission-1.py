class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] > intervals[i + 1][0]:
                if intervals[i][1] > intervals[i + 1][1]:
                    intervals.pop(i)
                else:
                    intervals.pop(i + 1)
                res += 1
            else:
                i += 1

        return res