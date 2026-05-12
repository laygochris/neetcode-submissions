class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        abc1, abc2 = [0] * 26, [0] * 26
        for i in range(len(s1)):
            abc1[ord(s1[i]) - ord('a')] += 1
            abc2[ord(s2[i]) - ord('a')] += 1

        matches = 0
        for i in range(26):
            matches += 1 if abc1[i] == abc2[i] else 0
        print(matches)
        print(abc1)
        print(abc2)
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            # decrement left window by 1
            # get index of corresponding character then decrease freq from array
            index = ord(s2[l]) - ord('a')
            abc2[index] -= 1
            l += 1
            print("removing", s2[l])

            if abc2[index] == abc1[index]:
                matches += 1
            elif abc2[index] == abc1[index] - 1:
                matches -= 1

            index = ord(s2[r]) - ord('a')
            abc2[index] += 1
            print("adding", s2[r])
            if abc2[index] == abc1[index]:
                matches += 1
            elif abc2[index] == abc1[index] + 1:
                matches -= 1
            print(abc1)
            print(abc2)
            print(s2[l : r])
            print(matches)
        return matches == 26