class Solution:
    def climbStairs(self, n: int) -> int:
        def explore(i):
            if n==1:
                return 1
            if i==2:
                return 2
            if i==3:
                return 3
            return explore(i-1)+explore(i-2)
        return explore(n)