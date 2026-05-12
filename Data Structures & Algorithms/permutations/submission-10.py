class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        used = set()    
        
        def solve(curr):
            if len(curr) == n:
                res.append(curr.copy())
                return
            for i in nums:
                if i not in used:
                    curr.append(i)
                    used.add(i)
                    solve(curr)
                    curr.pop()
                    used.remove(i)
        
        solve([])
        return res