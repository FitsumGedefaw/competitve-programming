class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        n, m = len(heights), len(heights[0])
        def inBound(row, col):
            return 0 <= row < n and 0 <= col < m

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(row, col, threshold, visited):
            if row == n - 1 and col == m - 1:
                return True

            if (row, col) not in visited:
                visited.add((row, col))
                for rowChange, colChange in directions:
                    newRow, newCol = row + rowChange, col + colChange
                    if inBound(newRow, newCol):
                        if abs(heights[row][col] - heights[newRow][newCol]) <= threshold and dfs(newRow, newCol, threshold, visited):
                            return True
                return False

        def canReachDestination(k):
            return dfs(0, 0, k, set())
        
        left, right = 0, (10 ** 6)

        while left < right:
            mid = left + (right - left) // 2
            if canReachDestination(mid):
                right = mid
            else:
                left = mid + 1
        
        return right
            


            

            
            

        return dfs(0, 0)

                