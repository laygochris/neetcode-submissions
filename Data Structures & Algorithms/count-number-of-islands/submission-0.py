class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0

        def traverse(row, col):
            if (row >= ROWS or row < 0 or
                col >= COLS or col < 0 or
                grid[row][col] == '0'):
                    return

            grid[row][col] = '0'
            for dr, dc in DIRECTIONS:
                nr, nc = row + dr, col + dc
                traverse(nr, nc)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    traverse(r, c)
                    islands += 1

        return islands
                



                

