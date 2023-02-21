class Node:
    def __init__(self, val=0, next = None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage, None, None)
        self.curr_node = self.head
    def visit(self, url: str) -> None:
        self.curr_node.next = Node(url,None, self.curr_node)
        self.curr_node = self.curr_node.next

    def back(self, steps: int) -> str:
        ct = 0
        while ct < steps and self.curr_node.prev:
            self.curr_node = self.curr_node.prev
            ct += 1
            
        return self.curr_node.val

    def forward(self, steps: int) -> str:
        ct = 0
        while ct < steps and self.curr_node.next:
            self.curr_node = self.curr_node.next
            ct += 1
            
        return self.curr_node.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)