class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()

        # Adicionamos os tesouros na fila
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))
        
        directions = [
            (1, 0),   # baixo
            (-1, 0),  # cima
            (0, 1),   # direita
            (0, -1)   # esquerda
        ]

        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if(
                    (0 <= nr < rows) and 
                    (0 <= nc < cols) and 
                    (grid[nr][nc] == 2147483647)
                ):
                    grid[nr][nc] = grid[r][c] + 1
                    queue.append((nr, nc))


            
