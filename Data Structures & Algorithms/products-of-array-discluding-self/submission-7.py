class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = 1, 1
        output = [1] * (len(nums))

        for i, n in enumerate(nums):
            output[i] = pre
            pre *= n

        for i in range(len(output) -1, -1, -1):
            output[i] *= post
            post *= nums[i]

        return output

