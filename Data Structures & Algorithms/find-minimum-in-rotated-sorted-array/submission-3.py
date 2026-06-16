class Solution:
    def findMin(self, nums: List[int]) -> int:
        def binary(left,right):
            if left<=right:
                mid=left+(right-left)//2
                
                if nums[mid]<nums[right]:
                    return binary(left,mid)
                    
                else:
                    return binary(mid+1,right)
            return left
        return nums[binary(0,len(nums)-1)-1]