class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            m = (top + bot) // 2
            # if smallest is greater than target
            # nothing else past matters
            if matrix[m][0] > target:
                bot = m - 1
            elif matrix[m][-1] < target:
                top = m + 1
            else:
                break
        
        if not top <= bot:
            return False
        
        l, r = 0, COLS - 1
        row = (top + bot) // 2
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r = mid - 1 
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        
        return False

            