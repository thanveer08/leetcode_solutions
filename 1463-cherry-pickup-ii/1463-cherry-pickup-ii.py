class Solution:
    def cherryPickup(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[[-1]*n for _ in range(n)]for _ in range(m)]

        def f(r,c1,c2):
            if c1<0 or c1>n-1 or c2<0 or c2>n-1:
                return -1e8
            if dp[r][c1][c2] != -1:
                return dp[r][c1][c2]
            if r == m-1:
                return grid[r][c1] if c1== c2 else grid[r][c1]+grid[r][c2]
            maxi = -1e9
            for a in range(-1,2):
                for b in range(-1,2):
                    if c1 == c2:
                        res = grid[r][c1]+ f(r+1,c1+a,c2+b)
                    else:
                        res = grid[r][c1]+ grid[r][c2]+ f(r+1,c1+a,c2+b)        
                    maxi = max(maxi,res)
            dp[r][c1][c2] = maxi
            return maxi
        return f(0,0,n-1)                