class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # RECURSION
        # 3 * 2 * 1 = n!
        # O(n! permuations * n^2)
        if len(nums) == 0:
            return [[]]

        # get rid of first element every time
        perms = self.permute(nums[1:])
        res = []

        for p in perms:
            # adding a single element to a permutation is at most n
            # cause of this for loop

            # we are inserting n elements into each permutation
            for i in range(len(p) + 1):
                temp = p.copy()
                temp.insert(i, nums[0])
                res.append(temp)

        return res
