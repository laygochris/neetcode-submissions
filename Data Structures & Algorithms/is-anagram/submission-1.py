class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            # countS[c] = num of occurences of char c
            # countT.get(c, 0) = returns num of occurences for char c
            if countS[c] != countT.get(c, 0):
                return False
        return True
        # or return countS == countT