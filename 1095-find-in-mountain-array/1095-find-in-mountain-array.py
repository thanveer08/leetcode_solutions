# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        A = mountainArr
        n = A.length()
        l,r = 0 , n-1
        #to find peak
        while l<r:
            m = (l+r)//2
            if A.get(m) < A.get(m+1):
                l = m+1
            else:
                r = m
        peak = m
        l,r  = 0 , peak
        while l<=r:
            m =(l+r)//2
            if A.get(m) == target:
                return m
            elif A.get(m) > target:  
                r = m-1
            else:
                l = m+1
        l = peak+1
        r = n - 1
        while l<=r:
            m =(l+r)//2
            if A.get(m) == target:
                return m
            elif A.get(m) > target:  
                l = m+1
            else:
                r = m-1
        return -1        

