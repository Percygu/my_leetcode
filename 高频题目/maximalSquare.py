'''
求最大的正方形
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        res = 0
        for i in range(m):
            if matrix[i][0] == "1":
                dp[i][0] = 1
                res = max(res,dp[i][0])
        for i in range(n):
            if matrix[0][i] == "1":
                dp[0][i] = 1
                res = max(res,dp[0][i])
        for i in range(1,m):
            for j in range(1,n):
                if matrix[i][j] == '1':
                    dp[i][j] = 1 + min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
                    res = max(res,dp[i][j])
        return res * res
