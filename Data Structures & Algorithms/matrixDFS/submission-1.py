class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        
        def dfs(grid: list[list[int]], r: int, c: int, visit: set[tuple[int, int]]):
            ROW, COLS = len(grid), len(grid[0])
            if (min(r, c) < 0 or
                r == ROW or c == COLS or
                (r, c) in visit or
                grid[r][c] == 1):
                return 0
            if (r == ROW - 1 and c == COLS - 1):
                return 1
            
            visit.add((r, c))
            count = 0
            count += dfs(grid, r + 1, c, visit)
            count += dfs(grid, r - 1, c, visit)
            count += dfs(grid, r, c + 1, visit)
            count += dfs(grid, r, c - 1, visit)

            visit.remove((r, c))
            return count
        
        return dfs(grid, 0, 0, set())