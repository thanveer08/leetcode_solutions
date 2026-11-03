class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        n = len(coins)
        dp = [[-1]* (amount + 1)for _ in range(n)]

        def knapsack(ind,amount):
            if ind == 0:
                if amount% coins[ind] == 0:
                    return amount//coins[ind]
                else:
                    return 1e8    
            if dp[ind][amount] != -1:
                return dp[ind][amount]

            not_pick =  0 + knapsack(ind-1,amount)
            pick = 1e8
            if amount>= coins[ind]:
        
                pick = 1 + knapsack(ind,amount - coins[ind])        
            dp[ind][amount] = min(not_pick,pick)
            return dp[ind][amount] 
        if knapsack(n-1,amount) == 1e8:
            return -1
        else:
            return knapsack(n-1,amount)    
                