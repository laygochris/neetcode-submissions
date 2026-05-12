class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        abc1, abc2 = [0] * 26, [0] * 26
        matches = 0
        
        for i in range(len(s1)):
            abc1[ord(s1[i]) - ord('a')] += 1
            abc2[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            matches += 1 if abc1[i] == abc2[i] else 0

        l = 0
        for r in range(len(s1), len(s2)):
            print(matches)
            if matches == 26:
                return True
            
            # increment right
            index = ord(s2[r]) - ord('a')
            print("Adding", s2[r])
            abc2[index] += 1
            if (abc1[index] == abc2[index]):
                print("r++")
                matches += 1
            if (abc2[index] == abc1[index] + 1):
                print("r--")
                matches -= 1

            index = ord(s2[l]) - ord('a')
            print("Removing", s2[l])
            abc2[index] -= 1
            if (abc1[index] == abc2[index]):
                print("l++")
                matches += 1
            if (abc2[index] == abc1[index] - 1):
                print("l--")
                matches -= 1
            l += 1

        return matches == 26


        
