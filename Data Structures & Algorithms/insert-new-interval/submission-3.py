class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        saveLen = len(intervals)
        for i in range(saveLen):
            if newInterval[0] <= intervals[i][0]:
                intervals.insert(i, newInterval)
                break
        if saveLen == len(intervals):
            intervals.append(newInterval)

        i = 0
        while i < len(intervals) - 1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i] = [intervals[i][0], max(intervals[i][1], intervals[i+1][1])]
                intervals.pop(i + 1)
            else:
                i += 1

        return intervals
