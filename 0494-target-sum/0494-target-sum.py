class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        diff = target
        total = sum(nums)
        n = len(nums)
        if total - diff <0 or (total - diff)%2 != 0:
            return 0
        t = (total - diff)//2
        dp = [[-1]*(t+1) for _ in range(n)]

        def f(ind,t):
            if ind == 0:
                if t== 0 or t == nums[0]:
                    return 1
                if t== 0 and nums[0] == 0  :
                    return 2
                return 0
            if dp[ind][t]!= -1:
                return dp[ind][t]
            not_pick = f(ind-1,t)
            pick = 0
            if nums[ind]<= t:
                pick = f(ind-1,t-nums[ind])  
            dp[ind][t] = pick + not_pick
            return dp[ind][t]            
        return f(n-1,t)    