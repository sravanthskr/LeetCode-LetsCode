class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        max=0
        while left<right:
            value=min(height[left],height[right])*(right-left)
            if value>max:
                max=value
            if height[right]<height[left]: # to get maximum of water contained, move minimum value index
                right-=1
            else:
                left+=1
        return max