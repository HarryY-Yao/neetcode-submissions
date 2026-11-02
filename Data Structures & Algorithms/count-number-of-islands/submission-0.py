class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        
        islands = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(r, c):
            q = deque([(r, c)])
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            visited.add((r, c))

            while q:
                x, y = q.popleft()

                for (dx, dy) in directions:
                    if (0 <= x + dx < rows and 0 <= y + dy < cols 
                        and grid[x + dx][y + dy] == "1" 
                        and (x + dx, y + dy) not in visited):
                        q.append((x + dx, y + dy))
                        visited.add((x + dx, y + dy))

                

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    islands += 1
                    bfs(row, col)
                
        return islands






                    



        
        