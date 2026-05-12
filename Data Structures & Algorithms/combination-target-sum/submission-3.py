class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def solve(curr, currSum, idx):
            if currSum == target:
                res.append(curr.copy())
                return
            if idx >= len(nums) or currSum > target:
                return
            
            curr.append(nums[idx])
            currSum += nums[idx]
            solve(curr, currSum, idx)
            curr.pop()
            currSum -= nums[idx]

            solve(curr, currSum, idx + 1)

        solve([], 0, 0)
        return res