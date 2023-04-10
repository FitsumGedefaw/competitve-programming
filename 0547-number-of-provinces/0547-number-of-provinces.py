class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def traverse(vertex, visited, graph):
            if vertex not in visited:
                visited.add(vertex)
                for neighbour in graph[vertex]:
                    traverse(neighbour, visited, graph)
        
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            graph[i] = [j for j in range(len(isConnected[i])) if isConnected[i][j] != 0 and i != j] 
        
        visited = set()
        numOfProvinces = 0
        
        for city in graph:
            if city not in visited:
                numOfProvinces += 1
                traverse(city, visited, graph)
        
        return numOfProvinces
                
                
        
                
        
        
        
        