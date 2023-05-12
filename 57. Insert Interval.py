class Solution(object):
    def insert(self, intervals, newInterval):
        i = 0
        
        # Skip over all intervals before the newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1
        
        # Merge overlapping intervals with newInterval
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            intervals.pop(i)
        
        # Insert the merged newInterval
        intervals.insert(i, newInterval)
        
        return intervals
