class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid) # of rows
        n = len(grid[0]) # of cols
        dp = grid.copy()

        for i in range(m):
            for j in range(n):
                if i != 0 and j != 0:
                    dp[i][j] += min(dp[i-1][j], dp[i][j-1])
                elif i != 0:
                    dp[i][j] += dp[i-1][j]
                elif j != 0:
                    dp[i][j] += dp[i][j-1]
                else:
                    pass
        return dp[-1][-1]
