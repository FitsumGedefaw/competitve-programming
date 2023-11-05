class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            num, den = equations[i]
            graph[num].append((values[i], den))
            graph[den].append((1/values[i], num))

        def dfs(currNode, currCost, targetNode, visited):
            #print(currNode, targetNode)
            visited.add(currNode)
            if currNode == targetNode:
                return currCost
            for cost, child in graph[currNode]:
                if child not in visited:
                    res = dfs(child, cost, targetNode, visited)
                    if res:
                        return res * currCost
            return 0

        ans = []
        for src, dst in queries:
            if src not in graph:
                ans.append(-1)
            else:
                res = dfs(src, 1, dst, set())
                ans.append(res if res else -1)
        
        return ans
            
        
        