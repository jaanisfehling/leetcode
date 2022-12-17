class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1]] + [[] for _ in range(numRows-1)]
        for i in range(1, numRows):
            dp[i] = [1] + [dp[i-1][j] + dp[i-1][j+1] for j in range(len(dp[i-1])-1)] + [1]
        return dp            
