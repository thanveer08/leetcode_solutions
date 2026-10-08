class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        s= sum(nums)
        n= len(nums)

        if s%2 != 0:
            return False

        dp = [[-1]*((s//2)+1) for _ in range(n)]

        def f(i:int,target:int):
            if target == 0: return True
            if i == 0:
                if nums[i] == target:
                    return True
                return False
            if dp[i][target] != -1:
                return dp[i][target]    
            notpick = f(i-1,target)
            pick = False
            if target >= nums[i]:
                pick = f(i-1,target - nums[i])
            dp[i][target] = notpick or pick
            return dp[i][target]
        return f(n-1,s//2)

        