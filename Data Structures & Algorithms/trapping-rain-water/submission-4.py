class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        rmax=height[r]
        lmax=height[l]
        res=0
        while(l<r):
            lmax=max(lmax,height[l])
            rmax=max(rmax,height[r])
            if height[r]<height[l]:
                res+=max(0,rmax-height[r])
                r-=1
            else:
                res+=max(0,lmax-height[l])
                l+=1
        return res