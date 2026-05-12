class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        hashmap = {}

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        # append b/c there can be multiple keys that repeat the same amount of times
        for key, value in hashmap.items():
            freq[value].append(key)
            
        result = []        
        for i in range(len(freq) -1, -1, -1):
            for j in (freq[i]):
                result.append(j)
            if len(result) == k:
                return result

        