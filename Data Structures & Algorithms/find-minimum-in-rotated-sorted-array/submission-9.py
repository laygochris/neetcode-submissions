class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[l]

        # when you cut in half check where your mid point is 
        # compared to left and right
        while l <= r:
            if nums[l] <= nums[r]:
                res = min(nums[l], res)
                break
            
            m = (l + r) // 2
            # check if m is a new min
            res = min(res, nums[m])

            # we are the left increasing side of the array
            # therefore want to leave it alone to find smaller values
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return res


