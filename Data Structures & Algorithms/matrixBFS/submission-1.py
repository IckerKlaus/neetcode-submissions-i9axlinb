class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        queue = deque()
        queue.append((0, 0))
        visited.add((0, 0))

        lenght = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS -1 and c == COLS - 1:
                    return lenght
                
                direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in direction:
                    if (min(r + dr, c + dc) < 0 or
                        r + dr >= ROWS or c + dc >= COLS or
                        (r + dr, c + dc) in visited or
                        grid[r + dr][c + dc] == 1):
                        continue
                    queue.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            lenght += 1

        return -1