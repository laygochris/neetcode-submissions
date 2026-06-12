class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if total > target or i >= len(nums):
                return
            
            # include i
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])
            # pop after including
            curr.pop()

            # do not include i
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res


