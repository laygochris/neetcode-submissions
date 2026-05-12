class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, currArr, currSum):
            if currSum == target:
                res.append(currArr.copy())
                return
            if i >= len(nums) or currSum > target:
                return
            
            currArr.append(nums[i])
            dfs(i, currArr, currSum + nums[i])
            currArr.pop()

            dfs(i+1, currArr, currSum)

        dfs(0, [], 0)
        return res
            
            


            