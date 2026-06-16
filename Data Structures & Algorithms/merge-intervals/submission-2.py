class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals)
        res=[intervals[0]]
        intervals=intervals[1:]
        i=0
        while( i <=(len(intervals)-1)): 
            print(res,intervals[i])  
            if intervals[i][1]>=res[len(res)-1][0] and intervals[i][0]<=res[len(res)-1][1]:
                res[len(res)-1]=[min(intervals[i][0],res[len(res)-1][0]),max(intervals[i][1],res[len(res)-1][1])]
                i+=1
            else:
                res.append(intervals[i])
                i+=1
            
        
        if i==len(intervals)-1:
            res.append(intervals[i])
        return res
