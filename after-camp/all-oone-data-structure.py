class Node:
    def __init__(self):
        self.keys = set()
        self.next = None
        self.prev = None
    def addKey(self, key):
        self.keys.add(key)
    def removeKey(self, key):
        if key in self.keys:
            self.keys.remove(key)
    def getKey(self):
        if len(self.keys) == 0:
            return ""
        for key in self.keys:
            return key



class AllOne:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.keyCt = {}
        self.freqNode = {0: self.head}        

    def inc(self, key: str) -> None:
        
        if key not in self.keyCt:
            ct = 0
            self.keyCt[key] = 1

        else:
            ct = self.keyCt[key]
            self.keyCt[key] += 1

        node = self.freqNode[ct]
        if ct + 1 not in self.freqNode: #if there is not a bucket for storing keys with freq ct + 1
            newNode = Node()
            newNode.prev, newNode.next = node, node.next
            node.next, newNode.next.prev = newNode, newNode
            newNode.addKey(key)
            self.freqNode[ct + 1] = newNode
        else:
            nextNode = self.freqNode[ct + 1]
            nextNode.addKey(key)
        
        node.removeKey(key)
        if node != self.head and node.getKey() == "": #if previous node no longer stores keys with freq ct 
            node.prev.next = node.next
            node.next.prev = node.prev
            
            del self.freqNode[ct]
        

        
        

            
    def dec(self, key: str) -> None:
        ct = self.keyCt[key]
        self.keyCt[key] -= 1
        if self.keyCt[key] == 0:
            del self.keyCt[key]
        node = self.freqNode[ct] # the bucket that stored keys with count ct
        node.removeKey(key) 
        
        if ct - 1 not in self.freqNode:
            newNode = Node()
            newNode.prev = node.prev
            newNode.prev.next = newNode
            if node.getKey() == "":
                newNode.next = node.next
                del self.freqNode[ct]
            else:
                newNode.next = node
            newNode.next.prev = newNode
            newNode.addKey(key)
            self.freqNode[ct - 1] = newNode
        else:
            prevNode = self.freqNode[ct - 1]
            prevNode.addKey(key)
            if node.getKey() == "":
                prevNode.next = node.next
                node.next.prev = prevNode
                del self.freqNode[ct]    


    def getMaxKey(self) -> str:
        return self.tail.prev.getKey()

    def getMinKey(self) -> str:
        return self.head.next.getKey()
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()