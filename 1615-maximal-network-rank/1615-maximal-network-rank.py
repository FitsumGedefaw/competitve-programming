class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        if len(roads) == 0:
            return 0
        elif len(roads) == 1:
            return 1
        
        connectedCities = defaultdict(set)
        
        for city1, city2 in roads:
            connectedCities[city1].add(city2)
            connectedCities[city2].add(city1)
        
        connectedCities = [(city, connectedCities[city]) for city in connectedCities]
        connectedCities.sort(key = lambda x: len(x[1]))
        
        maxNumOfConn, nextMaxNumOfConn = len(connectedCities[-1][1]), len(connectedCities[-2][1])
        maxNetRank = maxNumOfConn
        
        print(connectedCities, maxNumOfConn, nextMaxNumOfConn)  
        for i in range(len(connectedCities)-2, -1, -1):
            print(len(connectedCities[i][1]) < nextMaxNumOfConn)
            if len(connectedCities[i][1]) < nextMaxNumOfConn:
                print(connectedCities[i][1], len(connectedCities[i][1]))
                return maxNetRank
            else:
                for j in range(len(connectedCities)-1, i, -1):
                    
                    if len(connectedCities[j][1]) < maxNumOfConn:
                        break
                    if connectedCities[i][0] in connectedCities[j][1]:
                        maxNetRank = len(connectedCities[i][1]) + maxNumOfConn - 1
                    else:
                        return maxNumOfConn + nextMaxNumOfConn
        
        return maxNetRank
                    