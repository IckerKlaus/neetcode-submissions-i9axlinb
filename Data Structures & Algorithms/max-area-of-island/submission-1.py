class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        area = 0

        def bfs(r, c):
            q = deque()
            res = 1
            visited.add((r, c))
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = dr + row, dc + col
                    if (0 <= r < ROWS and 0 <= c < COLS and
                        grid[r][c] == 1 and (r, c) not in visited):
                        res += 1
                        q.append((r, c))
                        visited.add((r, c))
            
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, bfs(r, c))
        
        return area