class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        def binary(left,right):
            if left<=right:
                mid=left+(right-left)//2
                mid_val=mountainArr.get(mid)
                if mid_val==target:
                    return mid
                left_val=binary(left,mid-1)
                if left_val!= -1:
                    return left_val
                right_val=binary(mid+1,right)
                if right_val!= -1:
                    return right_val
                return -1
            return -1
        return binary(0,mountainArr.length()-1)