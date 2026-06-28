class Solution:
    def mySqrt(self, x: int) -> int:
        def binary(left,right):
            if left<=right:
                mid=left+(right-left)//2
                if mid*mid<=x and (mid+1)*(mid+1)>x:
                    return mid
                elif mid*mid<x:
                    return binary(mid+1,right)
                else:
                    return binary(left,mid-1)
            return left
        return binary(0,x)