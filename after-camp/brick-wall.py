class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edgeFreq = defaultdict(int)
        edgeMaxFreq = 0 #max edge freq seen so far
        
        for row in wall:
            edgePos = 0
            for i in range(len(row) - 1):
                brickWidth = row[i]
                edgePos += brickWidth
                edgeFreq[edgePos] += 1
                if  edgeFreq[edgePos] > edgeMaxFreq:
                    edgeMaxFreq = edgeFreq[edgePos]

        return len(wall) - edgeMaxFreq
        


