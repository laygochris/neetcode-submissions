class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        count = {}
        res = []

        for n in nums:
            count[n] = count.get(n, 0) + 1

        for key, v in count.items():
            freq[v].append(key)
        
        for i in range(len(freq) -1, -1, -1):
            for j in (freq[i]):
                res.append(j)
            if len(res) == k:
                return res
