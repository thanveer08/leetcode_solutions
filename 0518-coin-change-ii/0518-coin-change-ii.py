class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n = len(coins)
        dp = [[0]*(amount+1) for _ in range(n)]
        
        '''
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
      
        return ans  '''

        #tabulation
        for target in range(amount + 1):
            dp[0][target] = int( target%coins[0] ==0)   

        for ind in range(1,n):
            for target in range(amount+1):
                not_pick = dp[ind-1][target]
                pick = 0
                if coins[ind]<= target:
                    pick = dp[ind][target -coins[ind]]

                dp[ind][target] = pick + not_pick
        return dp[n-1][amount]       





