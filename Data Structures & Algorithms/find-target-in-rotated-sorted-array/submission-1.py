class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            print(nums[m])
            if nums[m] == target:
                return m
            
            # left array
            if nums[m] >= nums[l]:
                # if on left array, check if target is within that range
                # if within that range, want to shift our pointers to that side
                if nums[l] <= target <= nums[m]:
                    r = m - 1
                # if its not in the range, we want to move past the left side
                else:
                    l = m + 1
            else:
                # if we are on the right side, check if target is within that range
                # if we are within the range on the right side, move pointers over
                # we are within the range on the RIGHT if target is greater 
                # than the middle point, but less than the right (max)??
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                # if we are not within the range on the right side, 
                # we want to go towards the left
                else:
                    r = m - 1
        
        return -1 