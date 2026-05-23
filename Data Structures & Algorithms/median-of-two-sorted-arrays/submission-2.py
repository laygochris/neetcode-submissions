class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binary search through A, the shorter array
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        # i = midpoint for A array
        # if constraints for both partitions are not met 
        # continue bs through A to find different cuts so that 
        # we are able to find the correct left half
        l, r = 0, len(A) - 1
        total = len(A) + len(B)
        half = total // 2
        while True:
            i = (l + r) // 2 # A
            j = half - i - 2 # B (-2 because j and i start at 0)

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # constraint met => correct cut
            if Aleft <= Bright and Bleft <= Aright:
                # even or odd
                if total % 2:
                    # get minimum btwn the two leftmost values on the right partition
                    return min(Aright, Bright)
                else:
                    # max btwn two rightmost values on left partition
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            # if A array is too big, have to shrink to get smaller values
            # making B get a bigger cut
            elif Aleft > Bright:
                r = i - 1
            # if B array is too big, have to increase size of A array
            # to get bigger values, making B smaller
            else:
                l = i + 1

