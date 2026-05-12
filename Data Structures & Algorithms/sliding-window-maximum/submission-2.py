class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # window = size k
        l = r = 0
        output = []
        q = collections.deque()

        while r < len(nums):
            # while there is a q and the new element is greater than rightmost element
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            # once we reach the window size
            # add to output and decrease l
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1

            r += 1

        return output