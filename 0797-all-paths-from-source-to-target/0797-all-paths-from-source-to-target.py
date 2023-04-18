class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        
        def traverse(node, path):
            path.append(node)
            
            if node == len(graph) - 1:
                ans.append(deepcopy(path))

                path.pop()
                return
            
            for neigh in graph[node]:
                traverse(neigh, path)
            
            path.pop()
        
        path = []
        traverse(0, path)
        return ans
        