class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1,0],[0,1],[-1,0],[0,-1]]
        maxArea = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            area = 1
            grid[r][c] = 0            

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if (nr >= ROWS or nc >= COLS or
                        nr < 0 or nc < 0 or 
                        grid[nr][nc] != 1):
                        continue
                    
                    area += 1
                    grid[nr][nc] = 0
                    q.append((nr, nc))

            return area


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))
        
        return maxArea
                
