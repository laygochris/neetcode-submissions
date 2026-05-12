class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for key, val in count.items():
            freq[val].append(key)

        result = []
        for i in range(len(freq) -1, -1, -1):
            for j in freq[i]:
                result.append(j)
            if len(result) == k:
                return result