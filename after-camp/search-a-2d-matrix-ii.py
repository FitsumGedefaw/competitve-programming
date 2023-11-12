class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Time: O(m + n)
        n, m = len(matrix), len(matrix[0])
        row = 0
        col = m - 1

        while row < n and col > - 1:
            if matrix[row][col] < target:
                row += 1
            elif matrix[row][col] > target:
                col -= 1
            else:
                return True

        return False


    