class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary(left,right):
            if left<=right:
                mid=left+(right-left)//2
                print(mid)
                if nums[right]==target:
                    return right
                if nums[left]==target:
                    return left
                if nums[mid]==target :
                    return mid
                elif nums[mid]>nums[right] and (target<nums[right] or target>nums[mid]):
                    return binary(mid+1,right)
                else:
                    return binary(left,mid-1)
            return -1
        return binary(0,len(nums)-1)