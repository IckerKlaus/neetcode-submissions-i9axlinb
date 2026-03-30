class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # inicio/fin bloqueados
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        q = deque([(0, 0)])
        visited = {(0, 0)}
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,-1),(-1,1)]
        length = 1  # contamos celdas, no aristas

        while q:
            for _ in range(len(q)):  # nivel actual: todas las celdas a distancia 'length'
                r, c = q.popleft()
                if r == n - 1 and c == n - 1:
                    return length
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0 and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        q.append((nr, nc))
            length += 1

        return -1
