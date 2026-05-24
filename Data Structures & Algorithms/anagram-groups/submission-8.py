class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            abc = [0] * 27
            for c in s:
                abc[ord(c) - ord('a')] += 1
            if tuple(abc) in anagrams:
                anagrams[tuple(abc)].append(s)
            else:
                anagrams[tuple(abc)].append(s)

        return list(anagrams.values())