class Solution:
    def trap(self, height: List[int]) -> int:
        output = 0
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if height[l] < height[r]:
                l += 1
                leftMax = max(leftMax, height[l])
                output += leftMax - height[l]
            else:
                r -= 1 
                rightMax = max(rightMax, height[r])
                output += rightMax - height[r]
            
        return output
