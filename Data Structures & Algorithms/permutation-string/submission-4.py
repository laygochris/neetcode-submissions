class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        abc1, abc2 = [0] * 26, [0] * 26
        matches = 0
        # key: character, value: frequency
        for i in range(len(s1)):
            abc1[ord(s1[i]) - ord('a')] += 1
            abc2[ord(s2[i]) - ord('a')] += 1

        # comparing the entire array
        for i in range(26):
            matches += (1 if abc1[i] == abc2[i] else 0)

        l = 0
        print(matches)
        for r in range(len(s1), len(s2)):
            if matches == 26: return True

            # need to increment and decrement window
            # update frequencies in s2 array
            # index: need to get corresponding ASCII value of new character
            index = ord(s2[r]) - ord('a')
            abc2[index] += 1
            if (abc2[index] == abc1[index]):
                matches += 1
            if (abc2[index] == abc1[index] + 1):
                matches -= 1

            index = ord(s2[l]) - ord('a')
            abc2[index] -= 1
            l += 1
            if (abc2[index] == abc1[index]): 
                matches += 1
            if (abc2[index] == abc1[index] - 1):
                matches -= 1
        
        return matches == 26
