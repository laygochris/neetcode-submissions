class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # bs to find target row
        # then bs through target row
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, (ROWS) - 1
        while top <= bot:
            row = (bot + top )// 2
            # last element of middle row is TOO small
            # if last element is too small, eliminate all previous rows
            if matrix[row][-1] < target:
                top = row + 1
            # first element of middle row is TOO big
            # if first element is too big, eliminate all upcoming rows
            elif matrix[row][0] > target:
                bot = row - 1
            else:
                # found target row OR no target row
                break

        if not top <= bot:
            return False
        
        l, r = 0, (COLS) -1
        # top + bot calculated in previous while loop
        row = (top + bot) // 2 
        while l <= r:
            m = (l + r) // 2
            if target > matrix[row][m]:
                l = m + 1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False



        
                        
                    


