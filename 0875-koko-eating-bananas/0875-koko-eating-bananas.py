class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        while left<= right:
            k  = (left+ right)//2
            hours = 0
            for p in piles:
                hours = hours + math.ceil(p/k)
            if hours <= h:
                
                res = min(k,res)
                right = k- 1
            else:
                left = k+1
        return res            
            
            