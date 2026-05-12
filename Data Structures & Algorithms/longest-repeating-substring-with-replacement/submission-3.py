class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # key: char, value: freq
        count = {}
        # result: longest string
        # l: left pointer
        # maxF: most freq char value
        result, l, maxf = 0, 0, 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            maxf = max(maxf, count[s[r]])
            # window too big -> too many replacements
            while ((r - l + 1) - maxf) > k:
                count[s[l]] -= 1
                l += 1

            result = max(result, r - l + 1)
        
        return result






        
            