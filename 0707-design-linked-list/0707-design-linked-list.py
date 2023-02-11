class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head

        while node != None:
            yield node
            node = node.next

    def get(self, index):
        temp = self.head
        i = -1
        
        while temp != None:
            i += 1
            if i == index:
                return temp.val
        
            else:
                temp = temp.next
            
        return -1
        
    def addAtHead(self, val):
        node = Node(val)
        
        node.next = self.head
        self.head = node

    def addAtTail(self, val):
        node = Node(val)
        
        if self.head == None:
            self.head = node
            
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            
            temp.next = node


    def addAtIndex(self, index: int, val):
        if index == 0:
            self.addAtHead(val)
        else:
            new_node = Node(val)
            i = -1
            prev_node = self.head

            for node in self:
                i += 1
                if i == index:
                    new_node.next = node
                    prev_node.next = new_node
                    return
                prev_node = node

            if index == i+1:
                self.addAtTail(val)
            else:
                return

    def deleteAtIndex(self, index):
        if index == 0:
            self.head = self.head.next

        else:
            i = -1
            prev_node = self.head

            for node in self:
                i += 1
                if i == index:
                    prev_node.next = node.next
                    return
                prev_node = node
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)