class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        res=0
        r=len(heights)-1
        lmax=heights[l]
        rmax=heights[r]
        while(l<r):
            lmax=max(lmax,heights[l])
            rmax=max(rmax,heights[r])
            res=max(res,min(lmax,rmax)*(r-l))
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return res

        