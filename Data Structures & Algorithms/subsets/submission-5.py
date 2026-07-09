class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        res = []

        def dfs(i):

            if i >= len(nums):
                return subsets.append(res[:])

            # include i
            res.append(nums[i])
            dfs(i + 1)

            # don't include i
            res.pop()
            dfs(i + 1)
        
        dfs(0)
        return subsets


        