class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        nums.sort()

        for i in range (len(nums)):
            if nums[i] > 0:
                break
            elif i > 0 and nums[i] == nums [i-1]:
                continue
            lo,hi = i+1,len(nums)-1
            while lo < hi:
                if nums[i] + nums [lo] + nums[hi]  == 0:
                    answer.append([nums[i],nums[lo],nums[hi]])   
                    lo = lo +1
                    hi = hi -1 
                    while lo < hi and nums [lo] == nums [lo-1]:
                        lo = lo + 1
                    while lo < hi and nums[hi]== nums [hi+1]  :
                        hi = hi -1
                elif nums[i] + nums [lo] + nums[hi] > 0:       
                    hi = hi - 1        
                else: 
                    lo = lo + 1
        return answer                    
