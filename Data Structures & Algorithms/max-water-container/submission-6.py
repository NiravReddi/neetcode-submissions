class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i=0
        j=len(heights)-1
        mn=0
        while(i<j):
            
            if min(heights[i],heights[j])*(j-i)>mn:
                mn=min(heights[i],heights[j])*(j-i)
            if heights[i]<heights[j]:
                i+=1

            elif heights[j]<=heights[i]:
                j-=1
                continue
            
        return mn

        