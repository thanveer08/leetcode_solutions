class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l,r = 0, len(height)-1
        while l<r:
            area = (r-l)* min(height[l],height[r])
            if height[l]> height[r]:
                r = r-1
            else:
                l = l+1
            max_area = max(max_area,area)
           
        return max_area             
        