class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area = []
        l,r = 0, len(heights)-1
        while l<r:
            if heights[l]<heights[r] or heights[l] == heights[r]:
                area.append(heights[l]*(r-l))
                l+=1
            elif heights[r]<heights[l]:
                area.append(heights[r]*(r-l))
                r-=1
        return max(area)