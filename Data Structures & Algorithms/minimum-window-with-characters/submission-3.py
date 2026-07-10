class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        countT, countS = {}, {}
        res = ""
        length = float('infinity')

        # key: char, value: freq
        for i in range(len(t)):
            countT[t[i]] = countT.get(t[i], 0) + 1

        have, need = 0, len(countT)

        l = 0
        for r in range(len(s)):
            # add new char to dict
            countS[s[r]] = countS.get(s[r], 0) + 1

            # if new character matches t, increment have
            if s[r] in countT and countT[s[r]] == countS[s[r]]:
                have += 1

            while have == need:
                if length > r - l + 1:
                    length = r - l + 1
                    res = s[l:r+1]

                countS[s[l]] -= 1
                
                if s[l] in countT and countT[s[l]] > countS[s[l]]:
                    have -= 1
                l += 1
        
        return res
        

            



        
