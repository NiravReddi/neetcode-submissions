class Solution:
    def mySqrt(self, x: int) -> int:
        res=0
        def binary(left,right):
            nonlocal res
            if left<=right:
                mid=left+(right-left)//2
                if (mid*mid)>x:
                    return binary(left,mid-1)
                elif (mid*mid)<=x:
                    res=mid
                    return binary(mid+1,right)
                else:
                    return mid
                
            return left
        binary(1,x)
        return res