class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(left,right):
            if left<=right:
                mid=left+(right-left)//2
                
                if nums[mid]==target:
                    return mid
                if nums[mid]<nums[right]:
                    if nums[mid]<=target<=nums[right]:
                        return binary(mid+1,right)
                    else:
                        return binary(left,mid-1)
                else:
                    if nums[left]<=target<=nums[mid]:
                        return binary(left,mid-1)
                    else:
                        return binary(mid+1,right)
            return -1
        return binary(0,len(nums)-1)
        