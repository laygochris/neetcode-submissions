class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i, a in enumerate(nums):
            # optimization
            if a > 0:
                break
            
            # skip duplicates
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                currSum = a + nums[l] + nums[r]
                if currSum > 0:
                    r -= 1
                elif currSum < 0:
                    l += 1
                else:
                    output.append([a, nums[l], nums[r]])
                    # update pointers
                    l += 1
                    r -= 1

                    # skip duplicates again and stay in range
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
            
        return output
