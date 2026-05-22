class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        l = length = longest = 0

        for r in range(len(s)):
            while s[r] in ss:
                ss.remove(s[l])
                l += 1
                length -= 1
            
            ss.add(s[r])
            length += 1
            longest = max(longest, length)

        return longest


