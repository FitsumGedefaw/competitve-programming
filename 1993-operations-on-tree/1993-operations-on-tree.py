class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.lockedNodes = defaultdict(int)
        self.tree = defaultdict(list)
        
        for child, _parent in enumerate(parent):
            self.tree[_parent].append(child)

    def lock(self, num: int, user: int) -> bool:
        if num not in self.lockedNodes:
            self.lockedNodes[num] = user
            return True
        return False
            
    def unlock(self, num: int, user: int) -> bool:
        if num in self.lockedNodes and self.lockedNodes[num] == user:
            del self.lockedNodes[num]
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        def checkAncestors(node):
            if node in self.lockedNodes:
                return True
            if node == -1:
                return False
            return checkAncestors(self.parent[node])
        
        def checkDescendants(node):
            if node in self.lockedNodes:
                return True
            for child in self.tree[node]:
                if checkDescendants(child):
                    return True
            return False
        
        def unlockDescendants(node):
            if node in self.lockedNodes:
                del self.lockedNodes[node]
            for child in self.tree[node]:
                unlockDescendants(child)
        
        if num not in self.lockedNodes and not checkAncestors(self.parent[num]) and checkDescendants(num):
            unlockDescendants(num)
            self.lockedNodes[num] = user
            return True
        return False

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)