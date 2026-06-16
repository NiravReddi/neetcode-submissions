"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)==0:
            return True
        inter=[]
        for i in range(len(intervals)):
            inter.append([intervals[i].start,intervals[i].end])
        intervals=sorted(inter)
        res=[[intervals[0][0],intervals[0][1]]]
        for i in range(1,len(intervals)):
            if res[-1][1]>intervals[i][0]:
                return False
            else:
                res.append([intervals[i][0],intervals[i][1]])
        return True