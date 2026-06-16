class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def binary(left,right):
            if left<=right:
                mid=left+(right-left)//2
                if nums[mid]==target:
                    return mid
                elif target<=nums[mid]:
                    return binary(left,mid-1)
                else:
                    return binary(mid+1,right)
            return left
        return binary(0,len(nums)-1)