class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float("infinity")

        while l <= r:
            if nums[l] < nums[r]:
                return min(res, nums[l])

            m = (l + r) // 2
            # left sorted array

            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                # if nums[m] is greater than we know
                # min will be on the right of m
                l = m + 1
            else:
                r = m - 1

        return res
            