class Solution:
    # dp approach
    # def climbStairs(self, n: int) -> int:
    #     dp = [0]*(n+1)
    #     dp[1] = 1
    #     dp[2] = 2
    #     for i in range(3,n+1):
    #         dp[i]=dp[i-1]+dp[i-2]
    #     return dp[n]
    # memory optimzed approach
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        prev2=1
        prev1=2
        for i in range(3,n+1):
            current=prev1+prev2
            prev2=prev1
            prev1=current
        return prev1
        