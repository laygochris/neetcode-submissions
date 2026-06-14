class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        permutation = []
        def dfs(n, used_numbers):
            if n >= len(nums):
                res.append(permutation[:])
                return

            for i in (nums):
                if i not in used_numbers:
                    used_numbers.add(i)
                    permutation.append(i)
                    dfs(n + 1, used_numbers)

                    used_numbers.remove(i)
                    permutation.pop()
        
        dfs(0, set())
        return res

            
                

                




            