class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        abc1, abc2 = [0]*26, [0]*26
        for i in range(len(s1)):
            abc1[ord(s1[i]) - ord('a')] += 1
            abc2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            if abc1[i] == abc2[i]:
                matches += 1

        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            idx = ord(s2[r]) - ord('a')
            abc2[idx] += 1
            if abc2[idx] == abc1[idx]:
                matches += 1
            if abc2[idx] == abc1[idx] + 1:
                matches -= 1

            idx = ord(s2[l]) - ord('a')
            abc2[idx] -= 1
            if abc2[idx] == abc1[idx]:
                matches += 1
            if abc2[idx] == abc1[idx] - 1:
                matches -= 1
            l += 1
        
        return matches == 26
        