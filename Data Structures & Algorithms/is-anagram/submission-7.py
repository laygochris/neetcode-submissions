class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # base case: if length of strings are not equal
        if (len(s) != len(t)):
            return False

        sTable = {}
        tTable = {}

        for char in s: 
            if char in sTable:
                sTable[char] += 1
            else:
                sTable[char] = 1

        for char in t: 
            if char in tTable:
                tTable[char] += 1
            else:
                tTable[char] = 1

        return sTable == tTable
        
                
