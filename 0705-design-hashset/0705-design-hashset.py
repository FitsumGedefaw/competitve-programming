class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class MyHashSet:

    def __init__(self):
        self.head = None

    def add(self, key: int) -> None:
        curr_node = self.head
        
        if curr_node == None:
            self.head = Node(key)
            return
        
        while curr_node.next:
            if curr_node.val == key:
                return
            
            curr_node = curr_node.next
            
        if curr_node.val == key:
            return
        else:
            curr_node.next = Node(key)

    def remove(self, key: int) -> None:
        if self.head == None:
            return
        if self.head.val == key:
            self.head = self.head.next
            return
        
        prev_node = self.head
        curr_node = self.head.next
        
        while curr_node:
            if curr_node.val == key:
                prev_node.next = curr_node.next
                return
            prev_node = curr_node
            curr_node = curr_node.next

    def contains(self, key: int) -> bool:
        curr_node = self.head
        
        while curr_node:
            if curr_node.val == key:
                return True
            curr_node = curr_node.next
        
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)