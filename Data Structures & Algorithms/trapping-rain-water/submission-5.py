class Solution:
    def trap(self, height: List[int]) -> int:
        result, l, r = 0, 0,  len(height) - 1
        mLeft, mRight = height[l], height[r]

        while l < r:
            if mLeft < mRight:
                result += mLeft - height[l]
                l += 1
                mLeft = max(mLeft, height[l])
                
            else:
                result += mRight - height[r]
                r -= 1
                mRight = max(mRight, height[r])

        return result

