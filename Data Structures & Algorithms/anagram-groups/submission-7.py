class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            abc = [0] * 27
            for c in s:
                abc[ord(c) - ord('a')] += 1
            seen[tuple(abc)].append(s)

        return list(seen.values())

