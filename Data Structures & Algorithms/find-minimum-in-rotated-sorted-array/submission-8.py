class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary(left,right):
            print(left,right)
            if left<=right:
                mid=left+(right-left)//2
                if mid==0 or mid==right :
                    return min(nums[right],nums[0])
                elif(nums[mid]<nums[mid-1] and nums[mid]<nums[mid+1]) :
                    return nums[mid]
                elif nums[mid]>nums[right]:
                    return binary(mid+1,right)
                else:
                    return binary(left,mid-1)
            return nums[left]
        return binary(0,len(nums)-1)
                