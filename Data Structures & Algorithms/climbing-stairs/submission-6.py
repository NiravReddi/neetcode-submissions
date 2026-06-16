class Solution:
    def climbStairs(self, n: int) -> int:
        def explore(i):
            if i == n:
                return 0
            if i == n-1:
                return 1
            if i == n-2:
                return 2
            return explore(i + 2) + explore(i+1)
          
            
        return explore(0)