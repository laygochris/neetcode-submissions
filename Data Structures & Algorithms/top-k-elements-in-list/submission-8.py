class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # +1 b/c w/o, the biggest index would be N-1 => if 
        # num repeated N times, would not be stored
        freq = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for key, v in count.items():
            freq[v].append(key)
        
        res = []
        for i in range(len(freq) -1, -1, -1):
            for v in freq[i]:
                res.append(v)
            if len(res) == k:
                return res

