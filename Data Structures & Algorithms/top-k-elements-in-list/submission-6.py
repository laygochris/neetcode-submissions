class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # + 1 b/c max repeat = k => len(nums) = k - 1 indices => k would not be accounted for (out of bounds)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1+ count.get(n, 0)
        for key, v in count.items():
            freq[v].append(key)

        result = []
        for i in range(len(freq) -1, -1, -1):
            for j in freq[i]:
                result.append(j)
            if len(result) == k:
                return result

