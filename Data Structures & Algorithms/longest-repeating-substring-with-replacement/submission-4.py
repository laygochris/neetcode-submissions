class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = maxF = res = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxF = max(maxF, count[s[r]])

            # want to increment l when the window 
            # of replacement is too big
            if ((r - l + 1) - maxF) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
            
