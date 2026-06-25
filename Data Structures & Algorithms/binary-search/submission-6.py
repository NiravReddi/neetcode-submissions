class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(left,right):

            if left<=right:
                mid=left+((right-left)//2)
                print(mid)
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    return binary(left,mid-1)
                else:
                    return binary(mid+1,right)
            return -1
        return binary(0,len(nums)-1)