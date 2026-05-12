class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case: strings not same length
        if (len(s) != len(t)):
            return False
        
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 1)
            countT[t[i]] = 1 + countT.get(t[i], 1)

        for char in s:
            if countS[char] != countT.get(char, 0):
                return False
        return True
