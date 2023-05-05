class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        
        def isExit(row, col):
            return row in [0, m-1] or col in [0, n-1]
        
        def inBound(row, col):
            return (0 <= row < m) and (0 <= col < n)
        
        queue = deque([(entrance[0], entrance[1], 0)])
        visited = set([(entrance[0], entrance[1])])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            row, col, dist = queue.popleft()

            if [row, col] != entrance and isExit(row, col):
                return dist
            
            for rowChange, colChange in directions:
                newRow, newCol = row + rowChange, col + colChange
                
                if inBound(newRow, newCol) and maze[newRow][newCol] != "+" and (newRow, newCol) not in visited: 
                    queue.append((newRow, newCol, dist + 1))
                    visited.add((newRow, newCol))
        
        return -1
                
            