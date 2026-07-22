class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        L = 0
        R = n - 1
        while L<=R:
            M =( L + R)//2
            if nums[M] == target:
                return M
            elif nums[M] > target:
                R = M-1
            else:
                L = M + 1
        return -1            
        