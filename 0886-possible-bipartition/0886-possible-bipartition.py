class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        def colorNodes(node, color):
            colors[node] = color
            
            for neighbour in graph[node]:
                if colors[neighbour] == color:
                    return False
                if colors[neighbour] == -1:
                    if colorNodes(neighbour, 1 - color) == False:
                        return False
                
            return True
                    
                    
        graph = defaultdict(list)
        for node1, node2 in dislikes:
            graph[node1].append(node2)
            graph[node2].append(node1)
            
        colors = [-1] * (n+1)
        for node in range(1, (n+1)):
            if colors[node] == -1:
                if colorNodes(node, 0) == False:
                    return False
        
        return True
            
        