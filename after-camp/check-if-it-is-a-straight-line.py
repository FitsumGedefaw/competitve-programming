class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        slope = ((y2 - y1) / (x2 - x1) ) if (x2 - x1) != 0 else "doesnotExist"

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            _slope = ((y - y1) / (x - x1)) if (x - x1) != 0 else "doesnotExist"
            if _slope != slope:
                return False

        return True
        