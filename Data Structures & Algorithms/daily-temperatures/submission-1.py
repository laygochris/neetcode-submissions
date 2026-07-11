class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # store value, index

        for i, t in enumerate(temperatures):
            # pop when new idx > stack[-1]
            while stack and t > stack[-1][0]:
                v, idx = stack.pop()
                res[idx] = i - idx
            stack.append([t, i])

        return res
