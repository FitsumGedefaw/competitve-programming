class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def inBound(row, col):
            return (0 <= row < n) and (0 <= col < m)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = []
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 2:
                    queue.append((row, col))

        
        timeElapsed = 0
        while queue:
            temp = deque(queue)
            queue = []
            while temp:
                row, col = temp.popleft()
                for rowChange, colChange in directions:
                    newRow = row + rowChange
                    newCol = col + colChange

                    if inBound(newRow, newCol) and grid[newRow][newCol] == 1:
                        queue.append((newRow, newCol))
                        grid[newRow][newCol] = 2

            if not queue:
                break
            timeElapsed += 1
        
        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    return -1

        return timeElapsed

        
        

            
        
        