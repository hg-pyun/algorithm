class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class FirstUnique:
    
    def __init__(self, nums: List[int]):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.node_map = {}
        
        for value in nums:
            self.add(value)
        
    def insertToTail(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
    
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def showFirstUnique(self) -> int:
        if self.head.next == self.tail:
            return -1
        else:
            return self.head.next.val
        
    def add(self, value: int) -> None:
        if value in self.node_map:
            n = self.node_map.get(value)
            if n != None:
                self.removeNode(n)
            self.node_map[value] = None
        else:
            new_node = Node(value)
            self.insertToTail(new_node)
            self.node_map[value] = new_node
    
# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
