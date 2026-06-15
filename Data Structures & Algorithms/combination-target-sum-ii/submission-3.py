class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if total > target or i == len(candidates):
                return
            
            #include i and duplicates
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])

            #skip duplicates and do NOT include i
            while (i + 1) < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            curr.pop()
            dfs(i + 1, curr, total)
        
        dfs(0, [], 0)
        return res
            




