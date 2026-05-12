class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = set()
        n = len(nums)

        def solve(curr):
            if len(curr) == n:
                res.append(curr.copy())
                return
            for i in range(n):
                if nums[i] not in used:
                    curr.append(nums[i])
                    used.add(nums[i])
                    solve(curr)
                    curr.pop()
                    used.remove(nums[i])

        solve([])
        return res
                    


                
