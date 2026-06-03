class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = float('-inf')

        while l < r:
            newArea = (r - l) * min(heights[l], heights[r])
            area = max(area, newArea)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return area
