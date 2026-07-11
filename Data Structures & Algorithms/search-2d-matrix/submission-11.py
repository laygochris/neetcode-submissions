class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bottom = 0, ROWS - 1

        while top <= bottom:
            m = (top + bottom) // 2
            if matrix[m][0] > target:
                bottom = m - 1
            elif matrix[m][-1] < target:
                top = m + 1
            else:
                break

        if top > bottom: return False
        
        row = (top + bottom) // 2
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] == target: return True
            elif matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1

        return False
