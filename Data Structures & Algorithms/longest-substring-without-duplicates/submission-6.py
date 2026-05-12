class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        l, length = 0, 0
        for r in range(len(s)):
            while s[r] in ss:
                ss.remove(s[l])
                l += 1
            length = max(length, r - l + 1)
            ss.add(s[r])
        return length