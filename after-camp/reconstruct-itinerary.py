class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for source, destination in sorted(tickets, reverse=True):
            graph[source].append(destination)

        ans = []

        def dfs(node):
            while graph[node]:
                dfs(graph[node].pop())
            ans.append(node)
            
        
        #print("g", graph)
        dfs("JFK")
        return ans[::-1]
            

        