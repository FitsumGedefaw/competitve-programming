class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        coordinate = [None] * ((n**2)+1 )
        label = 1
        cols = [i for i in range(n)]
        for row in range(n-1, -1, -1):
            for col in cols:
                coordinate[label] = (row, col)
                label += 1
            cols.reverse()
        queue = deque([1])
        dist = [-1] * (n**2 + 1)
        dist[1] = 0
        
        while queue:
            label = queue.popleft()
            
            for nextLabel in range(label+1, min(label+7, (n**2)+1)):
                row, col = coordinate[nextLabel]
                dest = board[row][col] if board[row][col] != -1 else nextLabel
                
                if dist[dest] == -1:
                    dist[dest] = dist[label] + 1
                    queue.append(dest)
                    
        return dist[n**2]
                        
                
                
                
        