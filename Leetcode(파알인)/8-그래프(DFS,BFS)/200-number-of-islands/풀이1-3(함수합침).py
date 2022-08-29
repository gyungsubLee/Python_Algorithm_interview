class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if 0<=row<rows and 0<=col<cols and grid[row][col] == '1':
                grid[row][col] = '#'
                dfs(row+1, col)
                dfs(row-1, col)
                dfs(row, col+1)
                dfs(row, col-1)
            
        if not grid:
            return 0
        
        rows, cols, cnt = len(grid), len(grid[0]), 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    cnt += 1
        return cnt
    
    
        
        



            
            
        
        
            