class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        counter = {}

        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        for key, v in counter.items():
            freq[v].append(key)

        result = []
        for i in range(len(freq) -1, -1, -1):
            for j in freq[i]:
                result.append(j)
            if len(result) == k:
                return result


        