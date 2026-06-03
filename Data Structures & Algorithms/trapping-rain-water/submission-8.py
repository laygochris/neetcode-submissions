class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        mLeft, mRight = height[l], height[r]
        res = 0

        while l < r:
            if height[l] > height[r]:
                mRight = max(mRight, height[r])
                res += mRight - height[r]
                r -= 1
            else:
                mLeft = max(mLeft, height[l])
                res += mLeft - height[l]
                l += 1

        return res
