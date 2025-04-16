class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        nr, nc, num_islands = len(grid), len(grid[0]), 0
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(r, c):
            if 0 <= r < nr and 0 <= c < nc and grid[r][c] == "1":
                grid[r][c] = "0"
                for d_r, d_c in directions:
                    dfs(r + d_r, c + d_c)
                
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == "1":
                    num_islands += 1
                    dfs(r, c)
        
        return num_islands