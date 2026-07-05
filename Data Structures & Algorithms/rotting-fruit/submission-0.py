class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = rotten = time = 0
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        ROWS, COLS = len(grid), len(grid[0])
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    rotten += 1
                    q.append([r, c])
        
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr >= ROWS or nc >= COLS or 
                        nr < 0 or nc < 0 or 
                        grid[nr][nc] != 1):
                        continue
                    
                    fresh -= 1
                    grid[nr][nc] = 2
                    q.append([nr, nc])
            time += 1

        return time if fresh == 0 else -1





        
