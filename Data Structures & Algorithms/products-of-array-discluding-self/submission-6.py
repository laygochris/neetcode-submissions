class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # base case: len of array <= 2
        if len(nums) <= 2:
            return [nums[1], nums[0]]

        pre, post = 1,1 
        res = [1] * len(nums)
        for i, n in enumerate(nums):
            res[i] = pre
            pre *= n
        for i in range(len(res) -1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res