class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        r=float("inf")
        while(start<end):
            mid=(start+end)//2
            r=min(nums[mid],r)

            if nums[mid]>nums[end]:
                start=mid+1
            else:
                end=mid-1
        return min(r,nums[start])