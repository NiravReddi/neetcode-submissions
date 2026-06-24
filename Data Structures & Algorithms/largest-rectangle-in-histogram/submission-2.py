class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        res=0
        for r in range(len(heights)):
            start=r
            while(stack and stack[-1][1]>heights[r]):
                stind,stval=stack.pop()
                res=max(res,stval*(r-stind))
                start=stind
            stack.append((start,heights[r]))
        for i, h in stack:
            res = max(res, h * (len(heights) - i))
        return res