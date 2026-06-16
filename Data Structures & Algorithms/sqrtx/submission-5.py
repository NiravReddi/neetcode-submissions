class Solution:
    def mySqrt(self, x: int) -> int:
        def binary(left,right):
            if left<=right:
                mid=left+(right-left)//2
                if mid*mid <= x:
                    return binary(mid+1,right)
                else:
                    return binary(left,mid-1)
            return right
        return binary(1,x)
        