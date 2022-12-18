class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: return 0

        n = 50

        dp = [0 for _ in range(n)]
        dp[0] = x
        for i in range(1, n):
            dp[i] = 0.5 * (dp[i-1] + x/dp[i-1])
        return int(dp[-1])
