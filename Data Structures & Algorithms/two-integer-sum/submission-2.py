class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:    
        hashmap = {}
        for i, n in enumerate(nums):
            k = target - n
            if k in hashmap:
                return ([hashmap[k], i])
            hashmap[n] = i


            

                
        