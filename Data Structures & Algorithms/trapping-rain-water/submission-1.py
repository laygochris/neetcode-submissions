class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if height[l] < height[r]:
                leftMax = max(leftMax, height[l])
                output += leftMax - height[l]
                l += 1
            else:
                rightMax = max(rightMax, height[r])
                output += rightMax - height[r]
                r -= 1
        return output
            