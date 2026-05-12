class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in numMap:
                return ([numMap[diff], i])
            numMap[v] = i