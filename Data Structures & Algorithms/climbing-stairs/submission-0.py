class Solution:
    def climbStairs(self, n: int) -> int:
        # n = 2, 1+1 or 2 = 2
        # n = 3, 1+1+1 or 2+1 or 1+2 
        # n = 4, 1+1+1+1 or 2+1+1 or 1+2+1 or 1+1+2 or 2+2
        # n = 5, 1+1+1+1+1 or 2+1+1+1 or 1+2+1+1 or 1+1+2+1 or 1+1+1+2 or 2+2+1 or 1+2+2 or 2+1+2
        # n = 6, 1+1+1+1+1+1 or 2+1+1+1+1 or 1+2+1+1+1 or 1+1+2+1+1 or 1+1+1+2+1 or 1+1+1+1+2 or 2+2+1+1 or 2+1+2+1 or 2+1+1+2 or 1+2+1+2 or 1+1+2+2 or 2+2+2
        # ways(n) = ways(n-1) + ways(n-2)
        
        #base condition:
        if n==1: return 1
        if n==2: return 2

        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
