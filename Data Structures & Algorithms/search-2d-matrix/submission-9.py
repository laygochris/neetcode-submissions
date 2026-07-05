class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, btm = 0, len(matrix) - 1

        while top <= btm:
            m = (top + btm) // 2
            
            # if smallest pos at row is greater than target
            if matrix[m][0] > target:
                btm = m - 1
            # if greatest pos at row is less than target
            elif matrix[m][-1] < target:
                top = m + 1
            else:
                break
        
        if top > btm: return False
        

        row = (top + btm) // 2
        print(row)
        l, r = 0, len(matrix[m]) - 1
        print(l, r)
        while l <= r:
            m = (l + r) // 2
            print(m)
            if matrix[row][m] > target:
                r = m - 1
            if matrix[row][m] < target:
                l = m + 1
            if matrix[row][m] == target:
                return True
            
        return False





                
            


