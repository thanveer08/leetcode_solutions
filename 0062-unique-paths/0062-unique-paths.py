class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*n for _ in range(m)] 
        def f(row,col):
            if row == 0 or col == 0:
                return 1
            if dp[row][col] != -1:
                return dp[row][col]
            down = f(row-1,col)
            right = f(row,col-1)
            dp[row][col] = down + right
            return dp[row][col]

        
        return f(m-1,n-1)    