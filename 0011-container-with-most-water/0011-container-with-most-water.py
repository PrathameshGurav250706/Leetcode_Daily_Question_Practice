class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        low=0
        high=len(height)-1
        max_area=0
        while low<high:
            w=high-low
            h=min(height[high],height[low])
            area=w*h
            max_area=max(max_area,area)
            if height[low]<=height[high]:
                low+=1
            else:
                high-=1
        return max_area 

