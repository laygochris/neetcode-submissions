class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # keep track of nums and their frequency
        count = {}
        # num can repeat max N times => 
        # create array to store each num in its corresponding 
        freq = [[] for _ in range(len(nums) + 1)]
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for key, v in count.items():
            print(v)
            freq[v].append(key)
        
        result = []
        for i in range(len(freq) -1, -1, -1):
            for j in freq[i]:
                result.append(j)
            if len(result) == k:
                return result
