class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # base case: len(strs) <= 1
        if len(strs) <= 1:
            return [strs]

        # defaultdict automatically creates key default values 
        count = defaultdict(list)
        for s in strs:
            abc = [0] * 27
            for char in s:
                abc[ord(char) - ord('a')] += 1
            count[tuple(abc)].append(s)
        
        return list(count.values())
        