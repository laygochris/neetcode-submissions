class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # base case: 2 item array
        if (len(nums) == 2):
            return [nums[1], nums[0]]

        output = [1] * (len(nums))
        pre, post = 1, 1
        for i in range(len(nums)):
            output[i] = pre
            pre *= nums[i]
        for i in range(len(nums) -1, -1, -1):
            output[i] *= post
            post *= nums[i]
        return output
        
            
