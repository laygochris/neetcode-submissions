class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        for n in nums:
            new_perms = []
            for p in perms:
                print(p)
                for i in range(len(p) + 1):
                    print(i)
                    tmp = p[:]
                    print(tmp)
                    tmp.insert(i, n)
                    print(tmp)
                    new_perms.append(tmp)
                    #print(new_perms)
            perms = new_perms
        return perms