class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        self.maxArea = 0
        q = collections.deque()

        def bfs(r, c):
            grid[r][c] = 0
            q.append((r,c))
            area = 1

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (nr < 0 or nc < 0 or
                        nr >= ROWS or nc >= COLS or 
                        grid[nr][nc] != 1):
                        continue
                    
                    grid[nr][nc] = 0
                    area += 1
                    q.append((nr,nc))
            
            self.maxArea = max(self.maxArea, area)

        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    bfs(r, c)
        
        return self.maxArea