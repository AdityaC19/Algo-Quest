class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
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
        
    def insertAfterNode(self, node):
        after = self.head.next
        node.prev = self.head
        node.next = after
        after.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.deleteNode(node)
            self.insertAfterNode(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.deleteNode(node)
            self.insertAfterNode(node)
        else:
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                self.deleteNode(lru)
                self.cache.pop(lru.key)

            node = Node(key, value)
            self.insertAfterNode(node)
            self.cache[key] = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)