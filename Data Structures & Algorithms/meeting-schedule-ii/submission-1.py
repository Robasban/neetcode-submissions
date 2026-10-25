"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key=lambda x:x.end)
        final = intervals[-1].end

        trackTimes = [0] * (final + 1)
        for interval in intervals:
            for i in range(interval.start + 1, interval.end + 1):
                trackTimes[i] += 1
        
        return max(trackTimes)