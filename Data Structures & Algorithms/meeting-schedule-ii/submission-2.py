"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals)==0:
            return 0
        intervals.sort(key=lambda i: i.start)
        i=0
        d=1

        r=[]
        
        
        prevend=intervals[0].end
        intervals.pop(0)
        while(len(intervals)>0 ):
            print(r)
            if i==len(intervals):
                d+=1
                prevend=intervals[0].end

                intervals.pop(0)
                i=0
                continue
            elif intervals[i].start>=prevend:
                print("sds")
                r.append([intervals[i].start,intervals[i].end])
                prevend=intervals[i].end
                intervals.pop(i)
                continue
            i+=1
        return d
