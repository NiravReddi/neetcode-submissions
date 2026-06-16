class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mx=-1001
        r=0

        res=[]
        r1=[]
        while(r<k):
            mx=max(mx,nums[r])
            r1.append(nums[r])
            r+=1
        res.append(mx)
        while(r<len(nums)):
            r1.pop(0)
            r1.append(nums[r])
            res.append(max(r1))
            r+=1
        return res