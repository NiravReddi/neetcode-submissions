class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        lmax=height[l]
        rmax=height[r]
        res=0
        while(l<r):
            lmax=max(lmax,height[l])
            rmax=max(rmax,height[r])
            if height[l]<height[r]:
                res+=lmax-height[l]
                l+=1
            else:
                res+=rmax-height[r]
                r-=1
        return res


        