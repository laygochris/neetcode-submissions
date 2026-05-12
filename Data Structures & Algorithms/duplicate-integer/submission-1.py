class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked = set()
        for n in nums:
            if n in checked:
                return True
            else:
                checked.add(n)
        return False