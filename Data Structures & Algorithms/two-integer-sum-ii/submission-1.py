class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        output = []
        l, r = 0, len(numbers) - 1

        while l < r:
            newSum = numbers[l] + numbers[r]
            if newSum > target:
                r -= 1
            elif newSum < target:
                l += 1
            else:
                return [l + 1, r + 1]