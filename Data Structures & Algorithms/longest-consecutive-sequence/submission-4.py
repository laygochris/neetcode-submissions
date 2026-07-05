class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        length = 0

        for n in numSet:
            if (n - 1) not in numSet:
                seq = 1
                while (n + seq) in numSet:
                    seq += 1
                length = max(length, seq)
        
        return length