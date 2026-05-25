class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dick = deque()
        res = []
        l = 0
        for r in range(len(nums)):
            while dick and nums[r] > nums[dick[-1]]:
                dick.pop()

            dick.append(r)

            while l > dick[0]:
                dick.popleft()

            # we're at window, append max to output
            if (r - l + 1) == k:
                res.append(nums[dick[0]])
                l += 1

        return res
                
            
            

