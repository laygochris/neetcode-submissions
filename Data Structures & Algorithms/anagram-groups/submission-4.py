class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # base case: empty or 1 item array
        if len(strs) <= 1:
            return [strs]

        result = defaultdict(list)

        # assuming no special all lowercase letters
        for s in strs:
            abc = [0] * 26
            for c in s:
                # 'a' has lowest ascii value
                abc[ord(c) - ord("a")] += 1
            result[tuple(abc)].append(s)
        return list(result.values())