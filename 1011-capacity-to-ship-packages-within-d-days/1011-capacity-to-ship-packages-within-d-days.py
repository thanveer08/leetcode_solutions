class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        def check(capacity):
            day = 1
            current_weight = 0
            for w in weights:
                if current_weight + w > c:
                    current_weight = 0
                    day += 1
                current_weight += w
            return day<= days    


        while l<= r:
            c = (l+r)//2
            if check(c):
                res = min(c,res)
                r = c-1
            else:
                l = c+1   
        return res        

