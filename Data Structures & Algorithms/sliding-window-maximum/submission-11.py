class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # q holds max at given window
        q = collections.deque()
        res = []
        l = 0
        # deque holds indices
        for r in range(len(nums)):
            # if new element is greater than the 
            # rightmost element, keep popping
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            
            while (r - l + 1) == k:
                res.append(nums[q[0]])
                l += 1

        return res
