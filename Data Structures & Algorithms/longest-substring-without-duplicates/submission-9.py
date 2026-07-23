class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        length = l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            if (r - l + 1) > length:
                length = r - l + 1
        
        return length
