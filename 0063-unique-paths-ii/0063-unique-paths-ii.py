class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1]*n for _ in range(m)]
        def f(row,col):
            if row <0 or col < 0:
                return 0
            if obstacleGrid[row][col] == 1:
                return 0
            if row == 0 and col == 0:
                return 1

            if dp[row][col] != -1:
                return dp[row][col]

            down = f(row-1,col)
            right = f(row, col-1)

            dp[row][col] = down + right
            return dp[row][col]
        return f(m-1,n-1)                   
