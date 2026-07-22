class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        L = 0
        R = N-1
        while L<= R:
            M = (L+R)//2
            if nums[M] == target:
                return M
            elif nums[M]>= target:
                R = M - 1
            else:
                L = M + 1
        return L       