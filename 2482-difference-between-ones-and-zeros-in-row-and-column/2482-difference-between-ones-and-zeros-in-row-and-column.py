class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowMap, colMap = {},{}
        result = []
        for row in range(len(grid)):
            rowMap[row] = [0,0]
            for col in range(len(grid[0])):
                if col not in colMap:
                    colMap[col] = [0,0]
                if grid[row][col] == 1:
                    rowMap[row][1] += 1
                    colMap[col][1] += 1
                elif grid[row][col] == 0:
                    rowMap[row][0] += 1
                    colMap[col][0] += 1
        # print(colMap,"\n", rowMap)
        for row in range(len(grid)):
            array = []
            for col in range(len(grid[0])):
                array.append(rowMap[row][1]+colMap[col][1]-rowMap[row][0]-colMap[col][0])
            result.append(array)
        return result
