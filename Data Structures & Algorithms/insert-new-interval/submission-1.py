class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        idx = 0
        for interval in intervals:
            if interval[1] < newInterval[0]:
                res.append(interval)
                idx += 1
            elif newInterval[1] >= interval[0]:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]
                idx += 1
        res.append(newInterval)

        for i in range(idx, len(intervals)):
            res.append(intervals[i])

        return res
