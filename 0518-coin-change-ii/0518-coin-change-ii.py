class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = [[-1]*(amount+1) for _ in range(n)]
        def f(ind,target):
            if ind == 0:
                if target == 0 :
                    return 1
                if target%coins[0] ==0 :
                    return 1
                return 0
            if dp[ind][target]!= -1:
                return dp[ind][target]

            not_pick = f(ind-1,target)
            pick = 0
            if coins[ind]<= target:
                pick = f(ind,target -coins[ind])

            dp[ind][target] = pick + not_pick
            return dp[ind][target]   

        ans = f(n-1,amount)
      
        return ans                
