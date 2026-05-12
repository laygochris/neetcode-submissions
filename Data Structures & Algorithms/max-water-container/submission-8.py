class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        mArea = float("-infinity")

        while l <= r:
            area = (r - l) * min(heights[l], heights[r])
            mArea = max(mArea, area)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return mArea

    