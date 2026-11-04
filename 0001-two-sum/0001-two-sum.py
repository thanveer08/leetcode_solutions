class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # two pointers
        # i & j
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                if nums[i]+ nums[j] == target and i!=j:
                    return [i,j]
                    

        