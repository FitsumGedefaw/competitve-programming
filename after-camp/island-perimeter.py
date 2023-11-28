class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        perimetre = 0

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    if col + 1 >= m or grid[row][col + 1] == 0:
                        perimetre += 1
                    if col - 1 < 0 or grid[row][col - 1] == 0:
                        perimetre += 1
                    if row + 1 >= n or grid[row + 1][col] == 0:
                        perimetre += 1
                    if row - 1 < 0 or grid[row - 1][col] == 0:
                        perimetre += 1
        return perimetre

        