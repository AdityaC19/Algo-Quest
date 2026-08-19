class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head  
    
    def deleteNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
    
    def InsertAfterHead(self, node):
        afterNode = self.head.next
        node.prev = self.head
        node.next = afterNode
        self.head.next = node
        afterNode.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            self.InsertAfterHead(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.deleteNode(node)
            self.InsertAfterHead(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                self.deleteNode(lru)
                self.cache.pop(lru.key)
            new_node = Node(key, value)
            self.InsertAfterHead(new_node)
            self.cache[key] = new_node

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)