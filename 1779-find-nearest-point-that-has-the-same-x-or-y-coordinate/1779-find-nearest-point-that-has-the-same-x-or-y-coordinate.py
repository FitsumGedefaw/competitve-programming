class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        validPoints = []
        
        for index, point in enumerate(points):
            px, py = point
            if px == x or py == y:
                validPoints.append([index, px, py])
        
        if len(validPoints) == 0:
            return -1
                
        validPtsWithMD = []
        
        for point in validPoints:
            index, px, py = point
            MD = abs(px-x) + abs(py-y)
            
            validPtsWithMD.append([index, px, py, MD])
            
        validPtsWithMD.sort(key = lambda x: x[3])
        
        candidates = [pt for pt in validPtsWithMD if pt[3] == validPtsWithMD[0][3]]
        
        if len(candidates) == 1:
            return candidates[0][0]
        
        else:
            candidates.sort()
            return candidates[0][0]
        
            
            
        
                
                
                
                
            