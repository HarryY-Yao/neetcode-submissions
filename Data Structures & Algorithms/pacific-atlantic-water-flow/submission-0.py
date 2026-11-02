class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        
        pacific = set()
        atlantic = set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for i in range(cols):
            pacific.add((0, i))
            atlantic.add((len(heights) - 1, i))
        
        
        for i in range(rows):
            pacific.add((i, 0))
            atlantic.add((i, len(heights[0]) - 1))
        
        border_pacific = set(pacific)
        border_atlantic = set(atlantic)

        def dfs(r, c, visited):
            s = [(r, c)]

            while s:
                (x, y) = s.pop()

                for d in directions:
                    dx = x + d[0]
                    dy = y + d[1]
                    if (dx in range(rows) 
                    and dy in range(cols) 
                    and (dx, dy) not in visited
                    and heights[dx][dy] >= heights[x][y]):
                        visited.add((dx, dy))
                        s.append((dx, dy))

        for (x, y) in border_pacific:
            dfs(x, y, pacific)

        for (x, y) in border_atlantic:
            dfs(x, y, atlantic)

        return list(pacific & atlantic)


        



