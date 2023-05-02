class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def inBound(row, col):
            return (0 <= row < m) and (0 <= col < n)
        
        queue = deque()
        for row in range(m):
            for col in range(n):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = -1
            
        while queue:
            row, col = queue.popleft()

            for rowCh, colCh in directions:
                newRow = row + rowCh
                newCol = col + colCh

                if inBound(newRow, newCol) and mat[newRow][newCol] == -1:
                    mat[newRow][newCol] = mat[row][col] + 1
                    queue.append((newRow, newCol))       
                
        return mat
                
                