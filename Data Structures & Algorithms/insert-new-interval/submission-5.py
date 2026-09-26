class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        intput: list of intervals
        output: list of intervals with new interval in it

        edge cases: intervals is empty. newInterval overlaps with multiple intervals,
        newInterval appended at the end/front

        plan:
        iterate through intervals:
        if end of interval > start of newI, replace newI start with interval start
        otherwise, append interval to res
        if end of newI > start of interval and end of newI < end of interval, replace newI end with end of interval
            then append newinterval and the rest of the intervals to res
        """

        res = []
        k = 0
        while k < len(intervals):
            i = intervals[k]
            if i[1] < newInterval[0]:
                res.append(i)
            if i[0] > newInterval[1]:
                break
            
            if newInterval[0] >= i[0] and newInterval[0] <= i[1]:
                newInterval[0] = i[0]            
            if newInterval[1] >= i[0] and newInterval[1] <= i[1]:
                newInterval[1] = i[1]
                k += 1
                break
            k += 1

        res.append(newInterval)

        for i in range(k, len(intervals)):
            res.append(intervals[i])

        
        return res