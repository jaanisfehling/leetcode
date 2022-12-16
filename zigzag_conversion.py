class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        dp = [["" for _ in range(len(s))] for _ in range(numRows)]

        i = 0
        while len(s) > 0:
            # go down vertically
            if i % (numRows-1) == 0:
                for j, c in enumerate(s[:numRows]):
                    dp[j][i] = c
                    s = s[1:]
            # go up
            else:
                dp[-(i % (numRows-1))-1][i] = s[0]
                s = s[1:]
            i += 1
        
        res = ""
        for row in dp:
            for c in row: res += c
        return res

