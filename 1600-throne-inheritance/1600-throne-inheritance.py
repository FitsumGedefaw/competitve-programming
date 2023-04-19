class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.graph = defaultdict(list)
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        self.graph[childName] = []

    def death(self, name: str) -> None:
        self.dead.add(name)
    
    def getInheritanceOrder(self) -> List[str]:
        order = []
        
        def dfs(noble):
            if noble not in self.dead:
                order.append(noble)
            
            for child in self.graph[noble]:
                dfs(child)
        
        dfs(self.king)
        return order
            
            


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()