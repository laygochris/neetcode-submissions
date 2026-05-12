class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            while s != target:
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                s = numbers[l] + numbers[r]
            return [l + 1, r + 1]    
            
                
                


        